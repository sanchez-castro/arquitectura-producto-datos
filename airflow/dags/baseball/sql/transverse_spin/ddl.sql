CREATE TABLE IF NOT EXISTS `{{ params.project_id }}.baseball.{{ params.features_table }}` (
  game_pk INT64,
  at_bat_number INT64,
  pitch_number INT64,
  game_date DATE,
  pitcher_name STRING,
  pitcher INT64,
  pitch_type STRING,
  release_speed FLOAT64,
  release_spin_rate INT64,
  release_pos_x FLOAT64,
  release_pos_y FLOAT64,
  breakx FLOAT64,
  breakz FLOAT64,
  breakt FLOAT64,
  transverse_spin_measured INT64
)
PARTITION BY
  game_date
;
CREATE TABLE IF NOT EXISTS `{{ params.project_id }}.baseball.{{ params.predictions_table }}` (
  game_pk INT64,
  at_bat_number INT64,
  pitch_number INT64,
  game_date DATE,
  release_spin_rate INT64,
  breakx FLOAT64,
  breakz FLOAT64,
  transverse_spin_measured INT64,
  transverse_spin_predicted INT64,
  transverse_spin INT64,
  gyro_spin INT64
)
PARTITION BY
  game_date
;
