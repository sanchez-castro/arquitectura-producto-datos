INSERT INTO weather.daily_forecast (
    forecast_id,
    city_id,
    date,
    maxtemp_f,
    mintemp_f
)
VALUES (
  %s,  
  %s,
  %s,
  %s,
  %s
)
