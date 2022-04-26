CREATE TEMPORARY FUNCTION correctTransverseSpin(total_spin INT64, measured INT64, predicted INT64)
AS (
  CAST(CASE
    WHEN total_spin IS NULL THEN NULL
    WHEN total_spin < measured THEN LEAST(total_spin, predicted)
    WHEN measured < 0 THEN IF(predicted > 0, LEAST(predicted, total_spin), 0)
    WHEN ABS(measured - predicted) / measured >= 0.25 AND predicted > 0 THEN LEAST(predicted, total_spin)
    ELSE measured
  END as INT64)
);
TRUNCATE TABLE `{{ params.project_id}}.baseball.{{ params.predictions_table }}`;
INSERT INTO `{{ params.project_id}}.baseball.{{ params.predictions_table }}`
SELECT
  game_pk,
  at_bat_number,
  pitch_number,
  game_date,
  release_spin_rate,
  breakx,
  breakz,
  transverse_spin_measured as transverse_spin_measured,
  CAST(predicted_label as INT64) as transverse_spin_predicted,
  correctTransverseSpin(release_spin_rate, transverse_spin_measured, CAST(predicted_label as INT64)) as transverse_spin,
  CAST(SQRT(
    POW(release_spin_rate, 2)
    - POW(correctTransverseSpin(release_spin_rate, transverse_spin_measured, CAST(predicted_label as INT64)), 2)
  ) as INT64) as gyro_spin
FROM
  ML.PREDICT(
    MODEL `{{ params.project_id }}.baseball.transverse_spin_model_xgb20220402_v3`,
    TABLE `{{ params.project_id }}.baseball.{{ params.features_table }}`
  )
;
