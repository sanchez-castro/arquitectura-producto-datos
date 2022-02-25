# Class 5 Lab: Databases and ETL

## Objectives
- Configure Google Cloud SQL Databases
- Discover Database Security Options 
- Connect to a MySQL DB via Python
- Generate UUIDs in Python
- Normalize API request payload
- Insert API request payloads into DB tables

## Requirements
In order to follow along, the following will need to be installed:

- Python libraries:
  - notebook
  - [jupyterlab](https://jupyter.org/install)
  - pyyaml
  - [mysql](https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html)

We will also be using the [WeatherAPI](https://www.weatherapi.com/). While not required, it is recommended to sign up for a free account to acquire an API Key and follow along with the lab.

## Lab

In this lab, we will write an ETL script that extracts data from an API, transforms the payload, and loads it into a MySQL database. 

We will first create a MySQL database via Google Cloud SQL.

Then, we will once again be using the free WeatherAPI. We will use the historical weather API to get historical weather for the last 7 days from New York, Mexico City, and Houston. Feel free to use different cities, if you so choose. We will also write 

Finally, we'll transform our API payload 

### I. Configure Google Cloud SQL Database

First, let's create a new database instance via [Google Cloud SQL](https://cloud.google.com/sql). Cloud SQL is a fully managed, scaleable solution for hosting MySQL, Postgres, and SQL Server Databases. Specifically, the following are managed for you:

- Provisioning Hardware
- Installing DBMS run time on VMs
- Backups
- Encryption
- User Generation
- Networking and Security

Let's navigate to the [Cloud Console](https://console.cloud.google.com/sql) and begin.

0. If you do not already have the Cloud SQL API enabled on your Project, you will need to do this first. Don't worry: you will not be billed for enabling the API. 
1. Select Create Instance
2. Select your instance type and run time
    1. For this lab, we will be using a MySQL Database
    2. And we'll use version 8.0
3. Fill in your Instance Info
    1. Select an instance ID. This will be the name of your Cloud SQL Instance, not of the database itself. Don't worry too much about this ID. 
    2. Select the password for the root user. In general, I would recommend letting Google generate the password for you and do not store it. We will provision user accounts later. Do NOT share root user passwords with anyone.
    3. Under Database Version, select MySQL 8.0
4. Choose region and zonal availability
    1. We'll be using us-central1 for environmental reasons, but feel free to choose a region that is closer to you.
    2. For zonal availability, we will choose single zone as we don't need high availability for this demo and it costs less. In general, we do recommend multi-zone available when creating production databases, however.
5. Customize your instance
    1. Machine type: for this demo, let's use a lightweight instance with 1 CPU. For large databases, high memory is a better option.
    2. Storage: Select SSD and 10 GB. HDD is a cheaper, lower performance option. Also note that while we can enable automatic storage increases, you cannot decrease the size of your storage. Also note the "Advanced Encryption Option" to provide a customer-managed encryption key.
    3. Connections: In production, it is generally preferable to only allow private IP addresses. This restricts access to only computers on the same VPC as your database. For this demo, we will allow a public IP address. But, we can still restrict access through the allowed networks. Right now we will leave this blank and come back later when we create our DB users.
    4. Automated Backups: we will leave this on the default settings. Note how GCP manages DB backups for you. In an on-prem set up or user managed DB instance, you would have to create your own backups.
    5. Maintenance: we will leave this on the default settins. Note how GCP automates maitenance for you. In an on-prem set up or user managed DB instance, you would have to schedule and perform your own maitenance.
    6. We will leave flags empty for now.
    7. Under labels, let's add an environment label with the key-value `env: dev` so we now this is not a production database.

Now we can press `CREATE INSTNACE` and wait 3-5 minutes for our hardware to be provisioned and for our DB software to be installed. While we wait, let's dive into our security options. 

Now would also be a good time to install the python-mysql-connector if you have not already done so.


### II. Discover Database Security Options

Let's talk a little bit about our options for securing our database. In general, we would recommend one of four patterns:

1. Private IP Address, only
2. Public IP Address with Cloud IAM
3. Public IP Address with SSL
4. Pulic IP Address with whitelisting (encryption optional)

Only allowing a Private IP Address restricts access to your DB from computers in the same VPC. Access can also be allowed by authenticating through a VPN. This is the strictest security option you can select, and is generally recommended for Enterprise Companies. It is more strict than anything we will need today.

Allowing a Public IP Address allows access to your DB from the Internet. This is not as scary as it sounds. By default, no IP Addresses are whitelisted, which means even though your DB is accessible by the internet, no device may access it. You have three options for access control with a publically accessible database: IAM Roles, SSL, and whitelisting.

IAM Roles allow you to provision access to members of your GCP Project, only. This is a great option for accessing your DB from other GCP services as you can provide your VMs with the IAM Roles needed for querying your data. It also allows you to limit what actions certain users can take. For example, you can have read-only roles that can query data, but not create, edit, or delete tables. Remote (i.e. local) access is also feasible, but be careful with storing keys for doing so.  

SSL (Secure Socket Layer) is a technology for creating an encrypted link for transfering data. We can require SSL connections to our database, which will require all traffic to include SSL certification. This comes in the form of key files you can downloand from Google Cloud SQL. In general, we prefer security options that do not rely on key files as they can easily be lost or accidentally shared. Always, always store key files in secured Cloud Storage Buckets.

Finally, we can restrict traffic to our database by IP Address. We will be using this option for this demo. You can find your IP Address from [here](https://whatismyipaddress.com/). Then we'll create a new user in Google Cloud SQL that can only access our database from our IPv4 Address. Remember your username and password. We'll need that for our connection.

### III. Connect to a MySQL Database via Python

Now we're ready to connect to our Google Cloud SQL Instance. Let's take a look at [python-mysql-connector](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html) documentation.

In order to connect to our database, we'll need to:

1. Instantiate a mysql connector object
2. And pass it the public IP Address for our DB, along with our username and password

```python
import mysql.connector

cnx = mysql.connector.connect(
    user='scott', 
    password='password',
    host='127.0.0.1'
)
```

Recall from the APIs for Data lab that including passwords in code is a terrible practice. So we will include this information, as well as our API Keys from the WeatherAPI in a yaml file. Create a YAML File with that information and in the cell below, write the code needed to import our YAML file. You should:

1. Open the path to your yaml file
2. Store your yaml as a dict called "config"



```python
import yaml

config_file = open('labClass5.yaml', 'r')
config = yaml.safe_load(config_file)
```

In the cell below, import the mysql connector and instantiate a new connection with your config information from above.


```python
import mysql.connector

client = mysql.connector.connect(**config['connection'])
```

In the cell below, instantiate a new `cursor` object and execute the following query:
```sql
CREATE DATABASE weather
```


```python
cursor = client.cursor()
cursor.execute('CREATE DATABASE weather')
```

### IV. Generate UUIDs via Python
Recall from the Class 5 that we want need to replace repeated fields with an id. [UUIDs](https://docs.python.org/3/library/uuid.html) are a common and effective ID format. In the cell below, create a cities list where each element in the list is an object with two keys, `name` and `id` where the ID is a UUID. I will be using three cities: New York, Houston, and Mexico City. You may use any number of cities.


```python
import uuid

### Your Code Here

```

[Data Definition Language](https://www.techopedia.com/definition/1175/data-definition-language-ddl), or DDL, is SQL for creating new database tables. In the cell below, you will see the DDL needed to create a `cities` table with two fields: name and id. Both fields are of type variable character (VARCHAR), which are strings that can have up to a specified number of characters. Also note that to execute the query, we will use the our cursor's `execute()` method. 


```python
ddl = (
    "CREATE TABLE weather.cities("
    "name VARCHAR(255),"
    "id VARCHAR(40)"
    ")"
)
cursor.execute(ddl)
```

[Data Manipulation Language](https://www.techopedia.com/definition/1179/data-manipulation-language-dml), or DML, is SQL for adding or updating data in database tables. In the cell below, you will see the code needed to insert each of our cities into our new cities table. Note that in this case, we will pass to our cursor both our DML string and a tuple containing the names and IDs for each city.


```python
dml = (
    "INSERT INTO weather.cities ("
    "name,"
    "id"
    ")"
    "VALUES ("
    "%s,"
    "%s"
    ")"
)
for city in cities:
    cursor.execute(dml, (city['name'], city['id']))
```

To validate that our DML was successful, we will run a query to select each row from our cities table in the cell below. Note that we are using the `fetchall()` method to extract the results of our query.


```python
cursor.execute("SELECT * FROM weather.cities")
cursor.fetchall()
```

Finally, after verifying the data in our cities table, we have to commit the changes to our table using our MySQL client's `commit()` method.


```python
client.commit()
```

## BREAK

### V. Normalize API Request Payloads

Let's review. To this point we have:

1. Created a MySQL database via Google Cloud SQL
2. Connected to our database via python
3. Created a cities table in our database

Now that we know how to interact with our database, let's replicate the ETL process we ran in Lab 4, but write our API Request Payloads to a database table, rather than a CSV. Let's start by generating our request bodies. Free accounts for the Weather API can query historical data up to 7 days. The following code creates a list with the last 7 days as well as the components you need to create API calls for the history endpoint.

Where indicated, please append to the request_bodies list an API call body for each city in your cities dict and date in the dates list. Note that requests to the history endpoint are formatted as 

https://api.weatherapi.com/v1/history.json?key={weather_key}&q={city}&dt={date}


```python
import requests
from datetime import date, timedelta

weather_key = config['weather_key']
end = date.today()
start = end - timedelta(7)
dates = [str(start+timedelta(days=x)) for x in range((end-start).days)]
base_url = 'http://api.weatherapi.com/v1/'
history_api = 'history.json?' 
auth = f'key={weather_key}'


request_bodies = []
### Your Code Here

```

Great. Now that we have our request bodies, in the cell below:
1. Loop through each request body
2. Make a get request
3. Convert the request payload to a dict using the .json() method
4. And append the payload to the data list


```python
import requests


data = []
### Your Code Here

```

Now that we have our payloads, we need to once again parse them into the daily and hourly forecast. The following code loops through each element in our data and pulls out the city, date, and daily forecast. Given that we have three cities and seven days per city, we should end up with 21 elements in our forecast day list. 


```python
forecast_day = []
for row in data:
    for day in row['forecast']['forecastday']:
        forecast_day.append(
            {'city': row['location']['name'], 'date': day['date'], 'forecast': day['day']}      
        )
print(len(forecast_day))
```

In the cell below, replicate the process above for the hourly forecasts. Each element in the forecast_horu list should be a dict with the following keys:

- city
- date
- hour
- forecast

Because we have three cities, seven days per city, and 24 hours per day, we should end up with 504 elements in forecast_hour. 


```python
forecast_hour = []

### Your Code here

###
print(len(forecast_hour))
```

To normalize our request payloads, we need to add the corresponding city id to each object in our forecast_day and forecast_hour lists. 

In the cell below, write a for loop that for each object in forecast_day, appends a key `city_id` equal to the city_id corresponding to the city of that forecast.


```python
### Your Code Here

```

In the cell below, write a for loop that for each object in forecast_hour, appends a key city_id equal to the city_id corresponding to the city of that forecast.


```python
### Your Code Here

```

### VI. Insert API Request Payloads into Database Tables

Ok, now we're ready to write our request payloads to our MySQL Database. In the cell below, I am reading from the "create_daily_forecast.sql" file for my DDL. You may instead choose to write your DDL as a string like above. But it is generally preferable to read SQL files into your code than to include the SQL directly as string.


```python
with open("create_daily_forecast.sql") as ddl:
    cursor.execute(ddl.read())
```

Remember from the DML for our cities table that we need to pass our data into the cursor as a tuple. In the cell below, I am looping through the forecast_day list and for each day, creating a tuple with:

- A UUID to act as the primary key
- city_id
- Date
- Max Temp
- Min Temp

We would probably want to include additional fields if we were creating a full weather database, but this is enough for a demo.

Once we have our tuples ready, we can use the `executemany()` method, which applies a list of tuples to the our dml code. Also note that we are reading from the "insert_daily_forecast.sql" file for our DML.


```python
daily_forecast = []
for day in forecast_day:
    daily_forecast.append((
        str(uuid.uuid4()),
        day['city_id'], 
        day['date'], 
        day['forecast']['maxtemp_f'], 
        day['forecast']['mintemp_f'])
    )
    
with open("insert_daily_forecast.sql") as dml:
    cursor.executemany(dml.read(), daily_forecast)
```

Once we insert our rows, we'll need to commit the changes to our DB


```python
client.commit()
```

Now to verify the success of our DML, we'll run the following query to get the number of rows in our daily_forecast table. It should match the number of elements in our forecast_day list (21).

Note that the cursor.fetchall() method always returns a list of tuples. As such, we will need to first take the first element of the returned list and than the first element of that tuple to get a single number.


```python
query = 'SELECT COUNT(*) FROM weather.daily_forecast'
cursor.execute(query)
output = cursor.fetchall()
print(f"{output[0][0]} rows inserted")
```

In the cell below, please run the DDL to create the hourly forecast table, found in "create_hourly_forecast.sql"


```python
### Your Code Here

```

In the cell below, please run the DML to insert the data from forecast_hour into the newly created hourly_forecast table.


```python
### Your code Here

```

After running your code below, commit the changes in the cell below.


```python
client.commit()
```

Finally, run the cell below to verify your insert was successful. You should have inserted 504 rows (or however many records you had in your forecast_hour list.


```python
query = 'SELECT COUNT(*) FROM weather.hourly_forecast'
cursor.execute(query)
output = cursor.fetchall()
print(f"{output[0][0]} rows inserted")
```
