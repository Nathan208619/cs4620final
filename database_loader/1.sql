-- SELECT title, total_streams FROM most_streams JOIN most_streamed_artist ON most_streams.artist_id = most_streamed_artist.artist_id WHERE artist='Taylor Swift' ORDER BY total_streams DESC;
-- SELECT album, most_streamed_album.streams FROM most_streamed_album JOIN most_streamed_artist ON most_streamed_album.artist_id = most_streamed_artist.artist_id WHERE artist='Taylor Swift' ORDER BY most_streamed_album.streams DESC;
-- SELECT title, most_streams.daily_streams FROM most_streams JOIN most_streamed_artist ON most_streamed_artist.artist_id = most_streams.artist_id WHERE artist='Taylor Swift' ORDER BY most_streams.daily_streams DESC LIMIT 10;
-- SELECT artist, COUNT(title) FROM most_streams JOIN most_streamed_artist ON most_streams.artist_id = most_streamed_artist.artist_id GROUP BY artist ORDER BY COUNT(title) DESC LIMIT 10;
-- SELECT artist, COUNT(album) FROM most_streamed_album JOIN most_streamed_artist ON most_streamed_album.artist_id = most_streamed_artist.artist_id GROUP BY artist ORDER BY COUNT(album) DESC LIMIT 10;
-- SELECT artist, listeners FROM most_listeners JOIN most_streamed_artist ON most_listeners.artist_id = most_streamed_artist.artist_id ORDER BY listeners DESC LIMIT 10;
-- SELECT title, most_streams_of_year.total_streams FROM most_streams JOIN most_streams_of_year ON most_streams.streams_id = most_streams_of_year.song_id WHERE year=2020 ORDER BY most_streams_of_year.total_streams DESC LIMIT 10;
-- SELECT title, total_streams FROM most_streams WHERE total_streams != 0 ORDER BY total_streams ASC LIMIT 10;
SELECT total_streams FROM most_streams JOIN most_streamed_artist ON most_streams.artist_id = most_streamed_artist.artist_id WHERE artist='Kenshi Yonezu' ORDER BY total_streams;
```