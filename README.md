# Azure Postgresql Test

## Scope

When users complains about connectivity issues towards the Azure Database PostgreSQL endpoints, we developed a simple Python script that is continuously testing 
respective endpoint and save the timestamped output both in stdout and local file.

## Prerequisites

For running this script, we need to deploy a testing Pod on AKS cluster where we will upload our Python script along with the necessary libraries. For our testing, we used the classic nginx image.
We will start a nginx Pod and will connect to respective resource:

```
kubectl run nginx --image=nginx
kubectl exec -it nginx -- bash
```

We will need to install following packages on this pod:

python3
python3-pip
libpq-dev
psycopg2 (Python pip package Ex. pip install psycopg2)

After installing required packages and our script on the testing pod, we need to define the connectivity details used by testing script.
All these are exposed as environment variables as follows:

```
export PGHOST="your-db-fqdn.postgres.database.azure.com"
export PGUSER="your-configured"
export PGPASS="your-configured-password"
export DBNAME="database-name"
export TIMEINTERVAL="5" #Time interval in sec
```

After these variables configured, we can start our script with

```
python3 ./pgsql.py
```

If connection succeeds, we can see the following output:

```
07/11/2022 12:25:34 Connection established
``

Also, these information's are logged in the file named pgtest.log that can be shared in an emptyDir with the Node for data resiliency or any Azure Storage solution.

