# Class 4 Lab: APIs for Accessing Data

## Objectives
- Discover API documentation
- Store and Retrieve API keys in YAML file
- Make API calls in Python
- Parse GET request payloads
- Write request payload to CSV

## Requirements
In order to follow along, the following will need to be installed:

- Python libraries:
  - notebook
  - [jupyterlab](https://jupyter.org/install)
  - pyyaml

We will also be using the [WeatherAPI](https://www.weatherapi.com/). While not required, it is recommended to sign up for a free account to acquire an API Key and follow along with the lab.

## Lab

### I. Discover API Documentation
First, let's take a look at the [API Docs](https://www.weatherapi.com/docs/) for the free WeatherAPI.

When performing discovery on an API, look for answers to the following questions:

1. What endpoints are available and what data sources do they offer?
2. How is Authentication performed when making requests?
3. Is a software development kit (SDK) available?
4. How are requests to the API formatted?
5. How are request payloads formatted? What fields are included?

The WeatherAPI offers forecasted and historical weather data as well as location, astronomy, and other misc endpoints. For this lab, we will be focusing on current and forecasted weather. But feel free to explore the other endpoints available. Data is returned in json or xml format.

Authentication is performed via API Key. We can get one by signing up for a free account. In general, it is not a best practice to include API Keys directly in the code that is making the API request. We will cover storing and retrieving API Keys in the next section.

[SDKs](https://github.com/weatherapicom/) are available in several programming languages. SDKs are useful tools as they provide shortcuts and integrations for developing in the programming language of your choice. We will not be using the WeatherAPI SDK for this lab, but much of the code we will write for this lab has already been replicated in some form via the SDK. In general, use SDKs when they are available. They will save you time.

API Requests are formatted as follows:

`base url + <endpoint_name>.<file_extension> + auth + <query>`

With:

base url = `'http://api.weatherapi.com/v1/'`

auth = `'key=<api_key>'`

We'll look at some examples in Part III.

Finally, let's look at the docs for the forecast API. It looks like the payload contains three parts:
1. A day element containing the date and daily forecast information
2. An astro element sunrise and sunset data
3. An hour element containing the datetime and hourly forecast information

We'll explore these later on in the lab.

### II. Storing and Retrieving API Keys
[YAML](https://yaml.org/) (YAML Ain't Markup Language) is a human readable, [data-serialization](https://en.wikipedia.org/wiki/Serialization) language that is accessible to all programming languages. It is commonly used for config files as it is extremely easy to write due to it's lack of punctuation,

We can store our API key for the WeatherAPI in a yaml file like so:

```yaml
weather_key: <key>
```

We can then access our API key in python by using the pyyaml library.

We can do this by:

1. Importing pyyaml
2. Reading our config file
3. Converting the config file to a python dict via pyyaml and accessing the 'weather_key' element

```Python
import yaml
key_file = open('labClass4.yaml', 'r') #My config file for this lab
weather_key = yaml.safe_load(key_file)['weather_key']
```

### III. Making API Calls in Python
The Python [Requests](https://docs.python-requests.org/en/latest/) Library is a lightweight tool for making HTTP and API requests. It's also part of the Python standard library, making it easily accessible in all applications. Let's examine some of it's features by using the Current Weather endpoint from WeatherAPI.

Recall that we need the following components to make a GET request from WeatherAPI:

1. The base url: `'http://api.weatherapi.com/v1/'`
2. The Endpoint and return file format: `'current.json'`
3. Our API Key: `'key=<weather_key>'`
4. And our query, which will be the location for which we want the current weather

Here is an example from the API Docs: `http://api.weatherapi.com/v1/current.json?key=<YOUR_API_KEY>&q=London`
Notice how the pieces are combined:
1. There is a question mark ("?") between the endpoint and auth components
2. The query component begins with "q="
3. And there is an ampersand ("&") between the auth and query components.

We can thus parametrize our request as follows:

```python
base_url = 'http://api.weatherapi.com/v1/'
current_api = 'current.json?'
auth = f'key={weather_key}' #Using the weather key variable from the previous section
query = '11101' #My Zip Code
request_body = base_url + current_api + auth + f'&q={query}'
```

You might ask why we are storing our auth component as its own variable but use an [f-string](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/) for the query component in the request body. We do this because our query component will change depending on the API endpoint we use but our auth component will always be the same.

Now that we have our request body, let's make our first get request. We can do so by:
1. Importing the requests library
2. Using the `requests.get()` method and passing our body as a parameter.

```python
import requests
requests.get(request_body)
```

You should have received the following output:

`<Response [200]>`

That's great! A 200 code means your request was successfully. But now what? The Docs for the Requests library recommends storing your request as a variable so that you can easily access its methods and properties.

```Python
current_request = requests.get(request_body)
print(current_request.status_code) #Should return same 200 code
print(current_request.text) #Returns the body of the payload as a string
```

Awesome! Our request was successful and we can now access the payload. But something is still missing. Can you think of it?

Our payload is currently formatted as a string. It would be more useful if it was converted into an iterable class, like a dict. We can do so by using the built in JSON decoder, which converts JSON formatted strings into python dicts.

```Python
print(current_request.json())
print() #Newline
print(current_request.json()['location'])
print() #Newline
print(current_request.json()['location']['name'])
```

We'll take a deeper look at what we can do with our request payloads in the next section. But first, let's take a 5 minute break.

### Break

### IV. Parsing GET Request Payloads
Let's review. To this point, we have:
1. Reviewed the documentation for the WeatherAPI
2. Stored and retrieved our API Key
3. Parametrized our GET request body
4. Made a GET request to the Current Weather endpoint of the WeatherAPI
5. Converted the request payload into a python iterable.

That's a lot!

Now let's see what we can do with our request payloads. We'll be using the Forecast endpoint for this section as it has a lot more data in it than the Current endpoint. What changes will we need to make to our request body from Section 3?

We'll need to update the endpoint as well as our query. Requests to the Forecasts Endpoint are formatted like this:

`http://api.weatherapi.com/v1/forecast.json?key=<YOUR_API_KEY>&q=07112&days=7`

So now our query has two parameters: location and number of days. The free tier on WeatherAPI only allows forecasts of up to three days, so we will use the following for our request:

```python
forecast_api = 'forecast.json?'
query = {'zipcode': '11101', 'days': '3'}
```

Our query parameter is now a dict so we can keep all of it's components together. Using the above and the request body from Section 3, trying writing the body for our GET request.


```Python
request_body = base_url + forecast_api + auth + f"&q={query['zipcode']}&days={query['days']}"
print(request_body)
```

Great! Now like before, we can pass our request body into a GET request using the `requests.get()` method and convert it into an iterable using `.json()`.

```Python
forecast_request = requests.get(request_body).json()
print(forecast_request)
```

Ok! There's a lot more here now. If we remember back to Section 1, the Forecast Endpoint payload has three sections:

1. Day
2. Astro
3. Hour

We can more easily read our payload by using a [JSON Formatter](https://jsonformatter.curiousconcept.com/#) and feeding it our payload.

Interestingly, it seems calling the Forecast API also makes a get request to the Location and Current Endpoints as we have three nested objects:
- location
- current
- forecast

Inside the forecast object, we see an array of objects called 'forecastday'. Each forecastday object contains the date as well as a Day, Astro and Hour objects. The Hour object is an array containing forecast data for each hour of the day.

Let's start by isolating just the day and hour objects.

For the daily forecast, we can start by creating a blank list. Then we can loop through the our payload and append each day object as a new element in our list.

```python
forecast_day = [] # create an empty list
for day in forecast_request['forecast']['forecastday']: # loop through the forecastday array
    forecast_day.append(
        {'date': day['date'], 'forecast': day['day']} # append an object containing the date and forecast for each day       
    )
print(forecast_day)
```

Now let's repeat this process for the hourly forecast, which will be more complicated than the daily forecast. Recall the structure of our data:

```
- forecastday (array)
  - unnamed object (3x)
    - day (object)
      - daily forecast data
    - hour (array)
      - unnamed object (24x)
        - hourly forecast data
```

So now, we have to loop through each object in the forecast day array, and then loop through each element in the hour array contained in the elements. Specifically, for each of the 3 elements in forecastday, we want to pull out the 24 elements in hour. So we should end up with a python list containing 72 elements.

```python
forecast_hour = [] # create an empty list
for day in forecast_request['forecast']['forecastday']:  # loop through the forecastday array
    for hour in day['hour']: # loop through each hour array in forecast day
        forecast_hour.append(
            {'date': day['date'], 'hour': hour['time'], 'forecast': hour} # append an object contianing the date, hour, and forecast for each hour       
        )
print(len(forecast_hour)) # Check that we have 72 elements
print(forecast_hour[0]) # Let's just look at the first one
```  

Now that we've parsed our request payloads, we're ready to move on to the next step.

### V. Writing Request Payloads to .csv Files
The Python [csv](https://docs.python.org/3/library/csv.html) Library is a simple module for reading, writing, and interacting with csv files. It also provides classes for converting csv files to python dicts and vice versa.

We'll start by writing our daily forecast list to a CSV. The process is as follows:

1. Import the csv library
2. create a new csv file called 'daily_forecast.csv'
3. Instantiate a new csv.writer() object for our daily forecast, using our 'daily_forecast.csv' file as a target
4. Write a header row containing the names of our forecast fields
5. Loop through each element of our `forecast_day` list from Part IV
6. Write a new row in 'daily_forecast.csv' for each element in `forecast_day`

For this example, we'll use these fields:
1. Date
2. Max Temperature (in fahrenheit)
3. Min Temperature
4. Chance of rain
5. And weather conditions

The end result should be a csv file with 3 rows

```python
import csv
with open('daily_forecast.csv', 'w', newline = '') as file: # Create a new csv file named 'daily_forecast'
    daily_forecast = csv.writer(file, delimiter = ',') # Instantiate a csv.writer() object, writing to 'daily_forecast.csv'
    daily_forecast.writerow(['date', 'maxtemp_f', 'mintemp_f', 'avgtemp_f', 'daily_chance_of_rain','condition_text']) # Write the header for our csv file

    for day in forecast_day: # Loop through our forecast_day list and write the following fields in our csv file
            daily_forecast.writerow([
                day['date'],
                day['forecast']['maxtemp_f'],
                day['forecast']['mintemp_f'],
                day['forecast']['avgtemp_f'],
                day['forecast']['daily_chance_of_rain'],
                day['forecast']['condition']['text']
            ])
```

Now let's do the same for hourly forecast data. This is going to be easier with the work we did in Section IV. We would have to write two for loops if we hadn't created our forecast_hour object. Now we can replicate the process for writing the daily forecast csv with the fields from forecast_hour.

Recall one element in forecast_hour looks like this:

```python
{'date': '2022-01-16', 'hour': '2022-01-16 00:00', 'forecast': {'time_epoch': 1642309200, 'time': '2022-01-16 00:00', 'temp_c': -8.4, 'temp_f': 16.9, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 8.5, 'wind_kph': 13.7, 'wind_degree': 356, 'wind_dir': 'N', 'pressure_mb': 1029.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 28, 'cloud': 0, 'feelslike_c': -14.4, 'feelslike_f': 6.1, 'windchill_c': -14.4, 'windchill_f': 6.1, 'heatindex_c': -8.4, 'heatindex_f': 16.9, 'dewpoint_c': -23.7, 'dewpoint_f': -10.7, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 11.0, 'gust_kph': 17.6, 'uv': 1.0}}
```

Using the daily_forecast code block as an example, write a csv for the hourly forecast data with the following fields:

1. Date
2. Time
3. Temperature in fahrenheit
4. Humidity
4. Chance of rain  
5. Chance of snow
6. Visibility in kilometers
6. Wind speed in kph
6. Wind direction
6. Weather condition

Remember, there should be 72 rows.
