INSERT INTO weather.hourly_forecast (
  forecast_id,
  city_id,
  date,
  timestamp,
  temp_f,
  feelslike_f,
  chance_of_rain,
  chance_of_snow
)
VALUES (
  %s,  
  %s,
  %s,
  %s,
  %s,
  %s,
  %s,
  %s
)