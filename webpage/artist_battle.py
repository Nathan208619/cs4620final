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

def most_streamed_artist():
    conn = sqlite3.connect("music.db")
    query = "SELECT artist, streams FROM most_streamed_artist ORDER BY streams DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, streams = zip(*data)
    # create bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(artists, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Artists', fontsize=18)
    plt.ylabel('Streams', fontsize=18)
    title = "Top 10 Most Streamed Artist"
    plt.title(title, fontsize=25)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_battle/most_streamed_artists_bar.png')

    # create pie chart
    plt.figure(figsize=(15, 10))
    plt.pie(streams, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, textprops={'fontsize': 18})
    plt.axis('equal')
    title = "Top 10 Most Streamed Artists"
    plt.title(title, fontsize=25, y=1.05)
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_battle/most_streamed_artists_pie.png')

def most_streamed_artist_by_lead():
    conn = sqlite3.connect("music.db")
    query = "SELECT artist, stream_as_lead FROM most_streamed_artist ORDER BY stream_as_lead DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, streams = zip(*data)
    # create bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(artists, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Artists', fontsize=18)
    plt.ylabel('Streams', fontsize=18)
    title = "Top 10 Most Streamed Artists by Lead Streams"
    plt.title(title, fontsize=25)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_battle/most_streamed_artist_by_lead_bar.png')

    # create pie chart
    plt.figure(figsize=(15, 10))
    plt.pie(streams, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, textprops={'fontsize': 18})
    plt.axis('equal')
    title = "Top 10 Most Streamed Artists by Lead Streams"
    plt.title(title, fontsize=25, y=1.05)
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_battle/most_streamed_artist_by_lead_pie.png')

def most_streamed_artist_by_feature():
    conn = sqlite3.connect("music.db")
    query = "SELECT artist, stream_as_feature FROM most_streamed_artist ORDER BY stream_as_feature DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, streams = zip(*data)
    # create bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(artists, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Artists', fontsize=18)
    plt.ylabel('Streams', fontsize=18)
    title = "Top 10 Most Streamed Artists by Feature Streams"
    plt.title(title, fontsize=25)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_battle/most_streamed_artist_by_feature_bar.png')

    # create pie chart
    plt.figure(figsize=(15, 10))
    plt.pie(streams, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, textprops={'fontsize': 18})
    plt.axis('equal')
    title = "Top 10 Most Streamed Artists by Feature Streams"
    plt.title(title, fontsize=25, y=1.05)
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_battle/most_streamed_artist_by_feature_pie.png')

def most_streamed_artist_by_solo():
    conn = sqlite3.connect("music.db")
    query = "SELECT artist, streams_solo FROM most_streamed_artist ORDER BY streams_solo DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, streams = zip(*data)

    # create bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(artists, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Artists', fontsize=18)
    plt.ylabel('Streams', fontsize=18)
    title = "Top 10 Most Streamed Artists by Solo Streams"
    plt.title(title, fontsize=25)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_battle/most_streamed_artist_by_solo_bar.png')

    # create donut chart
    plt.figure(figsize=(15, 10))
    plt.pie(streams, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, textprops={'fontsize': 18})
    center_circle = plt.Circle((0, 0), 0.7, color='white', linewidth=0.5)
    plt.gca().add_artist(center_circle)
    plt.axis('equal')
    title = "Top 10 Most Streamed Artists by Solo Streams"
    plt.title(title, fontsize=25, y=1.05)
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_battle/most_streamed_artist_by_solo_donut.png')

def stacked_bar_chart():
    conn = sqlite3.connect("music.db")
    query = "SELECT artist, stream_as_lead, stream_as_feature FROM most_streamed_artist ORDER BY streams DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, stream_as_lead, stream_as_feature = zip(*data)

    bottom = [0] * len(artists)

    # make the stacked bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(artists, stream_as_lead, color='blue', label='Lead', edgecolor='black', bottom=bottom)
    bottom = [bottom[i] + stream_as_lead[i] for i in range(len(bottom))]

    # Plotting bars for feature streams
    plt.bar(artists, stream_as_feature, color='orange', label='Feature', edgecolor='black', bottom=bottom)
    bottom = [bottom[i] + stream_as_feature[i] for i in range(len(bottom))]

    # Plotting bars for solo streams
    # plt.bar(artists, streams_solo, color='green', label='Solo', edgecolor='black', bottom=bottom)
    plt.xticks(rotation=28, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.legend()
    plt.xlabel('Artists', fontsize=18)  
    plt.ylabel('Streams', fontsize=18)
    plt.title('Streams Breakdown for Top 10 Artists', fontdict={'fontsize': 25})
    plt.savefig('./static/visualizations/artist_battle/stacked_bar_chart.png')

def most_streamed_artist_by_daily_streams():
    conn = sqlite3.connect("music.db")
    query = "SELECT artist, daily_streams FROM most_streamed_artist ORDER BY daily_streams DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, streams = zip(*data)
    # create bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(artists, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Artists', fontsize=18)
    plt.ylabel('Streams', fontsize=18)
    title = "Top 10 Most Streamed Artists by Daily Streams"
    plt.title(title, fontsize=25)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_battle/most_streamed_artists_by_daily_streams_bar.png')

def top_10_artists_by_listeners():
    conn = sqlite3.connect("music.db")
    query = "SELECT artist, listeners FROM most_listeners ORDER BY listeners DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, listeners = zip(*data)
    
    # make bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(artists, listeners, color=cm.Paired.colors, edgecolor='black', linewidth=2)
    plt.xlabel('Artists' , fontsize=18)
    plt.ylabel('Number of Monthly Listeners', fontsize=18)
    title = "Top 10 Artists by Monthly Listeners"
    plt.title(title, fontsize=25)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_battle/top_10_artists_by_listeners_bar.png')

most_streamed_artist()
most_streamed_artist_by_daily_streams()
most_streamed_artist_by_lead()
most_streamed_artist_by_feature()
most_streamed_artist_by_solo()
stacked_bar_chart()
top_10_artists_by_listeners()