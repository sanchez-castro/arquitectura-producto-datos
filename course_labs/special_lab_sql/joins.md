```sql
/*
Which team mascot scored the most points in the 2017 season?
Find the top 100.
*/

SELECT 
  mascots.name,
  SUM(games.points) as total_points
FROM 
  `bigquery-public-data.ncaa_basketball.mascots` as mascots 
    JOIN bigquery-public-data.ncaa_basketball.mbb_teams_games_sr as games 
      ON mascots.id = games.team_id
WHERE 
  games.season = 2017
GROUP BY 1
ORDER BY 2 DESC 
LIMIT 100
```
