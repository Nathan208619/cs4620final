SELECT title, artist, total_streams
FROM most_streams
WHERE artist = 'Ed Sheeran' AND streams_id <= 100;

SELECT artist, SUM(total_streams)
FROM most_streams
WHERE artist = 'Ed Sheeran' AND streams_id <= 10