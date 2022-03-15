### From how many seasons do we have data?
```sql
SELECT DISTINCT 
  season
FROM 
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
ORDER BY
  1
```

### How many games were played in each season? How many teams were there? How many players played in at least one game? 10?
```sql
SELECT 
  season,
  COUNT(DISTINCT game_id) as count_games,
  COUNT(DISTINCT team_id) as count_teams,
  COUNT(DISTINCT player_id) as count_players,
  COUNT(DISTINCT IF(played, player_id, NULL)) as count_players_who_played
FROM 
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
GROUP BY 
  season
ORDER BY 
  season
```

```sql
WITH player_games AS (
SELECT 
  player_id,
  season,
  COUNT(game_id) as games_played
FROM 
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
WHERE 
  played
GROUP BY 
  1,2
)
SELECT 
  season,
  COUNT(player_id) as count_players
FROM 
  player_games
WHERE 
  games_played >= 10
GROUP BY season
```
### How many times in each season was a player active for a game but did not play?

```sql
SELECT 
  season,
  SUM(
    IF(
        active IS TRUE AND played IS FALSE,
        1,
        0
    )    
  ) as count_active_not_played,
FROM 
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
GROUP BY 
  season
```
