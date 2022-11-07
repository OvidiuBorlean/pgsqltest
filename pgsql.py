# Pre-requsites 
# apt install python3 
# apt install python3-pip
# apt install  libpq-dev
# pip install psycopg2

import psycopg2
import os
import time
from datetime import datetime


def checkPostgresql (host, user, dbname, password):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    sslmode = "require"
    try:
      conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
      conn = psycopg2.connect(conn_string) 
      print(dt_string + " " + "Connection established")
      conn.close()
      file1= open("pgtest.log","a") 
      content = dt_string + " " + "Connection established"
      file1.write(content)
      file1.write("\n")
      file1.close()
    except Exception as error:
      print(error)
      print("Connection Failure")
      file1= open("redis.log","a")
      content = dt_string + " " + "Connection Failure"
      file1.write(content)
      file1.write("\n")
      file1.close()

if __name__ == '__main__':
  print("Starting PostreSql Connectivity Check:...")
  myHostname = os.getenv('PGHOST')
  myPGUser = os.getenv("PGUSER")
  myPassword = os.environ.get('PGPASS')
  myDB = os.environ.get('DBNAME')
  myPassword = os.environ.get('PGPASS')
  interval = os.environ.get('TIMEINTERVAL')
  while True:
    checkPostgresql(myHostname, myPGUser, myDB, myPassword)
    time.sleep(int(interval))

#cursor = conn.cursor()
# Drop previous table of same name if one exists

#cursor.execute("DROP TABLE IF EXISTS inventory;")
#print("Finished dropping table (if existed)")
# Create a table
#cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
#print("Finished creating table")
# Insert some data into the table
#cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
#cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
#cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
#print("Inserted 3 rows of data")
#conn.commit()
#cursor.close()
