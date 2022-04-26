DECLARE g FLOAT64;
DECLARE d INT64;
DECLARE start INT64;
DECLARE dplate FLOAT64;
DECLARE c0 FLOAT64;
SET g = 32.179;
SET d = 50;
SET start = 40;
SET dplate = 17/12;
SET c0 = 5.153*POW(10, -3);
INSERT INTO `{{params.project_id}}.baseball.{{ params.features_table }}`
WITH base AS (
  SELECT
    game_pk,
    at_bat_number,
    pitch_number,
    game_date,
    pitcher_name,
    pitcher,
    pitch_type,
    release_speed,
    release_spin_rate,
    release_pos_x,
    release_pos_z,
    release_pos_y,
    vx0,
    vy0,
    vz0,
    ax,
    ay,
    az,
    rv,
    launch_speed,
    woba_value,
    estimated_woba_using_speedangle,
    woba_denom
  FROM
    `{{ params.project_id }}.baseball.pitches`
  WHERE
    game_date = '{{ ds }}'
),
t_start AS (
  SELECT
    *,
     (-vy0 - sqrt(POW(vy0,2) - 2 * ay * (d - start))) / ay as tstart
  FROM
    base
),
initial_velocity AS (
  SELECT
    *,
    vx0 + ax * tstart as vxstart,
    vy0 + ay * tstart as vystart,
    vz0 + az * tstart as vzstart
  FROM
    t_start
),
t_40 AS (
  SELECT
    *,
    (-vystart - sqrt(POW(vystart, 2) - 2 * ay *(start - dplate))) / ay as t40
  FROM
    initial_velocity
),
v_bar as (
  SELECT
   *,
    vxstart + .5 * ax * t40 as vxbar,
    vystart + .5 * ay * t40 as vybar,
    vzstart + .5 * az * t40 as vzbar,
    SQRT(
      POW(vxstart + .5 * ax * t40, 2)
      + POW(vystart + .5 * ay * t40, 2)
      + POW(vzstart + .5 * az * t40, 2)
    ) as vbar
  FROM
    t_40
),
a_drag as (
  SELECT
    *,
    abs(ax * vxbar + ay * vybar + (az + g) * vzbar) / vbar as adrag
  FROM
    v_bar
),
a_mag as (
  SELECT
    *,
    ax + adrag * vxbar / vbar as amagx,
    ay + adrag * vybar / vbar as amagy,
    (az + adrag * vzbar / vbar) + g as amagz,
  FROM
    a_drag
),
break_xy as (
  SELECT
    *,
    .5 * amagx * POW(t40, 2) * 12 as breakx,
    .5 * amagz * POW(t40, 2) * 12 as breakz,
    SQRT(
      POW(amagx, 2)
      + POW(amagy, 2)
      + POW(amagz,2)
    ) as amag,
    SQRT(
      POW(amagx, 2)
      + POW(amagy, 2)
      + POW(amagz, 2)
    ) / (c0 * POW(vbar, 2)) as lift_coefficient
  FROM
    a_mag
),
breakTotal AS (
  SELECT
    *,
    0.4 * lift_coefficient / (1 - 2.32 * lift_coefficient) as spin_coefficient,
    SQRT( POW(breakx, 2) + POW(breakz, 2)) as breakt
  FROM
    break_xy
)
SELECT
  game_pk,
  at_bat_number,
  pitch_number,
  game_date,
  pitcher_name,
  pitcher,
  pitch_type,
  release_speed,
  release_spin_rate,
  release_pos_x,
  release_pos_y,
  ROUND(breakx, 1) as breakx,
  ROUND(breakz, 1) as breakz,
  ROUND(breakt, 1) as breakt,
  CAST(80 * spin_Coefficient * vbar AS INT64) as transverse_spin_measured
FROM
  breakTotal
