CREATE TABLE IF NOT EXISTS weather.daily_forecast (
  forecast_id VARCHAR(40),
  city_id VARCHAR(40),
  date DATE,
  maxtemp_f FLOAT(5,2),
  mintemp_f FLOAT(5,2)
)
