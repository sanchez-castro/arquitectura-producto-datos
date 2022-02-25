CREATE TABLE IF NOT EXISTS weather.hourly_forecast (
  forecast_id VARCHAR(40),
  city_id VARCHAR(40),
  date DATE,
  timestamp DATETIME,
  temp_f FLOAT(5,2),
  feelslike_f FLOAT(5,2),
  chance_of_rain TINYINT,
  chance_of_snow TINYINT
)
