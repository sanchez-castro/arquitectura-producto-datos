```sql
/*
Calculate the rolling field goal percentage by season for each player
who played at least 500 minutes in a given season
and attempted at least 100 field goals
*/

SELECT 
  season,
  gametime,
  player_id,
  full_name,
  SUM(minutes_int64) OVER (PARTITION BY player_id, season) as total_minutes,
  SUM(field_goals_made) OVER (PARTITION BY player_id, season ORDER BY gametime ROWS BETWEEN 6 preceding and current row) as rolling_made,
  SUM(field_goals_att) OVER (PARTITION BY player_id, season ORDER BY gametime ROWS BETWEEN 6 preceding and current row) as rolling_att,
  SUM(field_goals_made) OVER (PARTITION BY player_id, season ORDER BY gametime ROWS BETWEEN 6 preceding and current row) / NULLIF(SUM(field_goals_att) OVER (PARTITION BY player_id, season ORDER BY gametime ROWS BETWEEN 6 preceding and current row), 0) as rolling_7fg_percentage,
  SUM(field_goals_made) OVER (PARTITION BY player_id, season ORDER BY gametime ROWS BETWEEN unbounded preceding and current row) as rolling_made_total,
  SUM(field_goals_att) OVER (PARTITION BY player_id, season ORDER BY gametime ROWS BETWEEN unbounded preceding and current row) as rolling_att_total,
  SUM(field_goals_made) OVER (PARTITION BY player_id, season ORDER BY gametime ROWS BETWEEN unbounded preceding and current row) / NULLIF(SUM(field_goals_att) OVER (PARTITION BY player_id, season ORDER BY gametime ROWS BETWEEN unbounded preceding and current row), 0) as rolling_fg_percentage
FROM 
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
WHERE 
  played
QUALIFY
  SUM(minutes_int64) OVER (PARTITION BY player_id, season) >= 500
    AND SUM(field_goals_att) OVER (PARTITION BY player_id, season) >= 100
```

```sql
/*
Calculate the rolling winning percentage, points scored, and points allowed per game
For each team in the top 100 in points scored per game
For the 2017 seasons
*/
```
