import sqlite3
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib.cm as cm

def query_the_database(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        # print(rows)
        return rows
    except sqlite3.Error as e:
        print(e)

# def top_ten_most_streamed_songs():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT title, total_streams FROM most_streams WHERE streams_id <= 10 ORDER BY total_streams DESC"
#     data = query_the_database(conn, query)
#     conn.close()
#     titles, streams = zip(*data)

#     # create bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(titles, streams, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Titles')
#     plt.ylabel('Streams')
#     title = f"Top 10 most streamed songs"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test3.png')

# def top_ten_least_streamed_songs():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT title, total_streams FROM most_streams ORDER BY total_streams ASC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     titles, streams = zip(*data)

#     # create scatter plot
#     plt.figure(figsize=(15, 10))
#     cmap = get_cmap("Set1")
#     colors = cmap(range(len(titles)))
#     plt.scatter(titles, streams, color=colors, edgecolor='black', s=250)
#     plt.xlabel('Titles')
#     plt.ylabel('Streams')
#     title = f"Top 10 least streamed songs"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test4.png')

# def top_ten_most_streamed_songs_of_year(year):
#     conn = sqlite3.connect("music.db")
#     query = "SELECT title, total_streams FROM most_streams_of_" + year + " WHERE streams_id <= 10 ORDER BY total_streams DESC"
#     data = query_the_database(conn, query)
#     conn.close()
#     titles, streams = zip(*data)

#     # create bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(titles, streams, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Titles')
#     plt.ylabel('Streams')
#     title = f"Top 10 most streamed songs of 2023"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     file = year + ".png"
#     plt.savefig(file)

# def artists_with_most_songs_top_2000():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT artist, COUNT(title) FROM most_streams GROUP BY artist ORDER BY COUNT(title) DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     artists, songs = zip(*data)
#     # create pie chart
#     plt.figure(figsize=(15, 10))
#     plt.pie(songs, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
#     plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
#     title = "Artists with most songs in the top 2000"
#     plt.title(title, fontsize=20)
#     plt.tight_layout()
#     plt.savefig('test6.png')

#     # bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(artists, songs, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Artists')
#     plt.ylabel('Songs')
#     title = "Artists with most songs in the top 2000"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test7.png')

# def top_ten_most_streamed_albums():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT album, streams FROM most_streamed_album ORDER BY streams DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     albums, streams = zip(*data)
#     # create bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(albums, streams, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Albums')
#     plt.ylabel('Streams')
#     title = "Top 10 most streamed albums"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test8.png')

# def top_ten_least_streamed_albums():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT album, streams FROM most_streamed_album ORDER BY streams ASC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     albums, streams = zip(*data)
#     # create scatter plot
#     plt.figure(figsize=(15, 10))
#     cmap = get_cmap("Set1")
#     colors = cmap(range(len(albums)))
#     plt.scatter(albums, streams, color=colors, edgecolor='black', s=250)
#     plt.xlabel('Albums')
#     plt.ylabel('Streams')
#     title = "Top 10 least streamed albums among the top 200"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test9.png')

# def artist_with_the_most_albums_in_top_200():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT artist, COUNT(album) FROM most_streamed_album GROUP BY artist ORDER BY COUNT(album) DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     artists, albums = zip(*data)
#     # create pie chart
#     plt.figure(figsize=(15, 10))
#     plt.pie(albums, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
#     plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
#     title = "Artists with most albums in the top 200"
#     plt.title(title, fontsize=20)
#     plt.tight_layout()
#     plt.savefig('test10.png')

#     # bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(artists, albums, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Artists')
#     plt.ylabel('Albums')
#     title = "Artists with most albums in the top 200"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test11.png')

# def build_artist_top_songs_by_daily_streams(artist):
#     conn = sqlite3.connect("music.db")
#     query = "SELECT title, daily_streams FROM most_streams WHERE artist='" + artist + "' ORDER BY daily_streams DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     if data is None:
#         print(f"No data found for the artist: {artist}")
#         return
#     titles, daily_streams = zip(*data)

#     # Craft the and save the figure
#     plt.subplots(figsize=(15, 15))
#     # plt.figure(figsize=(15, 20))
#     plt.pie(daily_streams, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
#     plt.legend(titles, title='Track Legend', bbox_to_anchor=(1, 0.5), loc="center", fontsize='small')

#     plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
#     plt.title(f"{artist}'s top songs by daily streams", fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test12.png')

#     # create bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(titles, daily_streams, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Titles')
#     plt.ylabel('Streams')
#     title = f"{artist}'s top songs by daily streams"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test13.png')

# def artist_stream_stats(artist):
#     conn = sqlite3.connect("music.db")
#     query = "SELECT streams, stream_as_lead, stream_as_feature, streams_solo WHERE artist={artist}"
#     data = query_the_database(conn, query)
#     conn.close()
#     if data is None:
#         print(f"No data found for the artist: {artist}")
#         return
#     titles, daily_streams = zip(*data)

#     categories = ['LeadStreams', 'FeatureStreams', 'SoloStreams']
#     values = [400000, 200000, 400000]

#     plt.bar('TotalStreams', 1000000, color='lightgray')
#     plt.bar('TotalStreams', values, color=['skyblue', 'lightcoral', 'lightgreen'], bottom=0)
#     plt.xlabel('Streams')
#     plt.title('Streams Breakdown for Artist')
#     plt.show()

# def most_streamed_artist():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT artist, streams FROM most_streamed_artist ORDER BY streams DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     artists, streams = zip(*data)
#     # create bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(artists, streams, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Artists')
#     plt.ylabel('Streams')
#     title = "Top 10 most streamed artists"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test14.png')

#     # create pie chart
#     plt.figure(figsize=(15, 10))
#     plt.pie(streams, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
#     plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
#     title = "Top 10 most streamed artists"
#     plt.title(title, fontsize=20)
#     plt.tight_layout()
#     plt.savefig('test15.png')

# def most_streamed_artist_by_lead():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT artist, stream_as_lead FROM most_streamed_artist ORDER BY stream_as_lead DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     artists, streams = zip(*data)
#     # create bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(artists, streams, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Artists')
#     plt.ylabel('Streams')
#     title = "Top 10 most streamed artists as lead"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test16.png')

#     # create pie chart
#     plt.figure(figsize=(15, 10))
#     plt.pie(streams, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
#     plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
#     title = "Top 10 most streamed artists as lead"
#     plt.title(title, fontsize=20)
#     plt.tight_layout()
#     plt.savefig('test17.png')

# def most_streamed_artist_by_feature():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT artist, stream_as_feature FROM most_streamed_artist ORDER BY stream_as_feature DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     artists, streams = zip(*data)
#     # create bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(artists, streams, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Artists')
#     plt.ylabel('Streams')
#     title = "Top 10 most streamed artists as feature"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test18.png')

#     # create pie chart
#     plt.figure(figsize=(15, 10))
#     plt.pie(streams, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
#     plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
#     title = "Top 10 most streamed artists as feature"
#     plt.title(title, fontsize=20)
#     plt.tight_layout()
#     plt.savefig('test19.png')

# def most_streamed_artist_by_solo():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT artist, streams_solo FROM most_streamed_artist ORDER BY streams_solo DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     artists, streams = zip(*data)
#     # create bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(artists, streams, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Artists')
#     plt.ylabel('Streams')
#     title = "Top 10 most streamed artists as solo"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)
#     plt.tight_layout()
#     plt.savefig('test20.png')

#     # # create pie chart
#     # plt.figure(figsize=(15, 10))
#     # plt.pie(streams, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
#     # plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
#     # title = "Top 10 most streamed artists as solo"
#     # plt.title(title, fontsize=20)
#     # plt.tight_layout()
#     # plt.savefig('test21.png')

#     # create pie chart
#     plt.figure(figsize=(15, 10))
#     plt.pie(streams, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

#     # Draw a white circle in the center to create the donut hole
#     center_circle = plt.Circle((0, 0), 0.7, color='white', linewidth=0.5)
#     plt.gca().add_artist(center_circle)

#     plt.axis('equal')

#     title = "Top 10 most streamed artists as solo"
#     plt.title(title, fontsize=20)
#     plt.tight_layout()
#     plt.savefig('test21.png')

# def stacked_bar_chart():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT artist, stream_as_lead, stream_as_feature FROM most_streamed_artist ORDER BY streams DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     artists, stream_as_lead, stream_as_feature = zip(*data)

#     bottom = [0] * len(artists)

#     # make the stacked bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(artists, stream_as_lead, color='blue', label='Lead', edgecolor='black', bottom=bottom)
#     bottom = [bottom[i] + stream_as_lead[i] for i in range(len(bottom))]

#     # Plotting bars for feature streams
#     plt.bar(artists, stream_as_feature, color='orange', label='Feature', edgecolor='black', bottom=bottom)
#     bottom = [bottom[i] + stream_as_feature[i] for i in range(len(bottom))]

#     # Plotting bars for solo streams
#     # plt.bar(artists, streams_solo, color='green', label='Solo', edgecolor='black', bottom=bottom)
#     plt.xticks(rotation=45, ha='right', fontsize=15)
#     plt.legend()
#     plt.xlabel('Artists')
#     plt.ylabel('Streams')
#     plt.title('Streams Breakdown for Artist')
#     plt.savefig('test22.png')

# def most_streamed_artist_by_daily_streams():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT artist, daily_streams FROM most_streamed_artist ORDER BY daily_streams DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     artists, streams = zip(*data)
#     # create bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(artists, streams, color=cm.Paired.colors, edgecolor='black')
#     plt.xlabel('Artists')
#     plt.ylabel('Streams')
#     title = "Top 10 most streamed artists by daily streams"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
#     plt.tight_layout()
#     plt.savefig('test23.png')

# def top_10_artists_by_listeners():
#     conn = sqlite3.connect("music.db")
#     query = "SELECT artist, listeners FROM most_listeners ORDER BY listeners DESC LIMIT 10"
#     data = query_the_database(conn, query)
#     conn.close()
#     artists, listeners = zip(*data)
    
#     # make bar chart
#     plt.figure(figsize=(15, 10))
#     plt.bar(artists, listeners, color=cm.Paired.colors, edgecolor='black', linewidth=2)
#     plt.xlabel('Artists')
#     plt.ylabel('Listeners')
#     title = "Top 10 artists by listeners"
#     plt.title(title, fontsize=20)
#     plt.xticks(rotation=45, ha='right', fontsize=18)
#     plt.tight_layout()
#     plt.savefig('test24.png')

def plot_artist_songs_chart(artist):

    # query the database
    conn = sqlite3.connect("music.db")
    query = "SELECT title, total_streams FROM most_streams JOIN most_streamed_artist ON most_streams.artist_id = most_streamed_artist.artist_id WHERE artist='" + artist + "' ORDER BY total_streams DESC"
    
    data = query_the_database(conn, query)
    conn.close()
    if data is None:
        print(f"No data found for the artist: {artist}")
        return
    titles, daily_streams = zip(*data)

    # query the database
    plt.subplots(figsize=(25, 25))
    plt.pie(daily_streams, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, textprops={'fontsize': 21})
    plt.legend(titles, title='Track Legend', bbox_to_anchor=(1, 0.5), loc="center left", fontsize='large', title_fontsize='large')

    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('test1.png')

def plot_artist_album_chart(artist):
    conn = sqlite3.connect("music.db")
    query = "SELECT album, most_streamed_album.streams FROM most_streamed_album JOIN most_streamed_artist ON most_streamed_album.artist_id = most_streamed_artist.artist_id WHERE artist='" + artist + "' ORDER BY most_streamed_album.streams DESC"
    data = query_the_database(conn, query)
    conn.close()
    if data is None:
        print(f"No data found for the artist: {artist}")
        return
    titles, album_streams = zip(*data)
    
    # Create the bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(titles, album_streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Titles', fontsize=18)
    plt.ylabel('Album Streams', fontsize=18)
    title = f"{artist}'s most streamed albums among the top 200"
    plt.title(title, fontsize=20)    
    plt.xticks(rotation=30, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('test2.png')

def build_artist_top_songs_by_daily_streams(artist):
    conn = sqlite3.connect("music.db")
    query = "SELECT title, most_streams.daily_streams FROM most_streams JOIN most_streamed_artist ON most_streamed_artist.artist_id = most_streams.artist_id WHERE artist='" + artist + "' ORDER BY most_streams.daily_streams DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    if data is None:
        print(f"No data found for the artist: {artist}")
        return
    titles, daily_streams = zip(*data)

    plt.subplots(figsize=(15, 10))
    plt.pie(daily_streams, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, textprops={'fontsize': 18})
    plt.legend(titles, title='Track Legend', bbox_to_anchor=(1, 0.5), loc="center", fontsize='small', title_fontsize='medium')

    plt.axis('equal') 
    plt.title(f"{artist}'s top songs by daily streams", fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.tight_layout()
    plt.savefig('test3.png')

    # create bar chart
    plt.figure(figsize=(12, 10))
    plt.bar(titles, daily_streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Titles', fontsize=18)
    plt.ylabel('Streams', fontsize=18)
    title = f"{artist}'s top songs by daily streams"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('test4.png')


def main():
    artist = "Taylor Swift"
    plot_artist_songs_chart(artist)
    plot_artist_album_chart(artist)
    build_artist_top_songs_by_daily_streams(artist)

if __name__ == "__main__":
    main()
