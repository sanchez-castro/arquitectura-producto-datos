```sql
/*
Get the season averages for each player to play in at least 10 games. 
We want Points, Rebounds, Assists, Steals, and Blocks per game, 
field goal percentage, three point field goal percentage, effective field goal percentage, and free throw percentage
*/

SELECT 
  season,
  player_id,
  ROUND(AVG(Points), 1) as ppg,
  ROUND(AVG(rebounds), 1) as rpg,
  ROUND(AVG(assists), 1) as apg,
  ROUND(AVG(Steals), 1) as spg,
  ROUND(AVG(blocks), 1) as bpg,
  CONCAT(ROUND(100 * SUM(field_goals_made) / NULLIF(SUM(field_goals_att), 0), 1), "%") as fg_percentage
FROM 
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
WHERE 
  played IS TRUE
GROUP BY 
  season, player_id
HAVING 
  COUNT(game_id) >= 10
```

```sql
/*
Get the per 36 minute averages for each player to play at least 500 minutes. 
We want Points, Rebounds, Assists, Steals, and blocks per 36 minutes
*/

SELECT 
  season,
  player_id,
  ANY_VALUE(full_name) as player_name,
  ROUND(36 * SUM(points) / SUM(minutes_int64), 1) as pp36,
  ROUND(36 * SUM(rebounds) / SUM(minutes_int64), 1) as rp366,
  ROUND(36 * SUM(assists) / SUM(minutes_int64), 1) as ap36,
  ROUND(36 * SUM(blocks) / SUM(minutes_int64), 1) as bp36,
  ROUND(36 * SUM(steals) / SUM(minutes_int64), 1) as sp36
FROM 
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
WHERE 
  played IS TRUE
GROUP BY 
  season, player_id
HAVING 
  SUM(minutes_int64) >= 500 
```  
  
```sql  
/* 
How many players averaged more offensive rebounds than defensive rebounds per game? 
Min 100 minutes played
*/

WITH players AS (
SELECT 
  season,
  player_id
FROM 
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
WHERE  
  played
GROUP BY 
  1,2
HAVING 
  sum(minutes_int64) >= 100
    AND AVG(offensive_rebounds) > AVG(defensive_rebounds)
)
SELECT 
  season,
  COUNT(player_id) as count_players
FROM 
  players 
GROUP BY 
  season
```
