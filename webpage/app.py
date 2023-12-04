from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.cm as cm

app = Flask(__name__)

def query_the_database(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        # print(rows)
        return rows
    except sqlite3.Error as e:
        print(e)

# ---------ARTIST VISUALIZATIONS---------
def plot_artist_album_chart(artist):
    # Query the albums_streams table
    conn = sqlite3.connect("music.db")
    query = "SELECT album, streams FROM most_streamed_album WHERE artist=" + "'" + artist + "'"
    data = query_the_database(conn, query)
    conn.close()
    if data is None:
        print(f"No data found for the artist: {artist}")
        return
    titles, album_streams = zip(*data)
    
    # Create the bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(titles, album_streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Titles')
    plt.ylabel('Album Streams')
    title = f"{artist}'s most streamed albums among the top 200"
    plt.title(title, fontsize=20)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=12)  # Adjust the rotation angle as needed
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_albums.png')

def plot_artist_songs_chart(artist):

    # query the database
    conn = sqlite3.connect("music.db")
    query = "SELECT title, total_streams FROM most_streams WHERE artist=" + "'" + artist + "'"
    data = query_the_database(conn, query)
    conn.close()
    if data is None:
        print(f"No data found for the artist: {artist}")
        return
    titles, daily_streams = zip(*data)

    # query the database
    plt.subplots(figsize=(15, 12))
    plt.pie(daily_streams, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.legend(titles, title='Track Legend', bbox_to_anchor=(1, 0.5), loc="center", fontsize='small')

    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_songs.png')

def build_artist_top_songs_by_daily_streams(artist):
    conn = sqlite3.connect("music.db")
    query = "SELECT title, daily_streams FROM most_streams WHERE artist='" + artist + "' ORDER BY daily_streams DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    if data is None:
        print(f"No data found for the artist: {artist}")
        return
    titles, daily_streams = zip(*data)

    plt.subplots(figsize=(10, 8))
    plt.pie(daily_streams, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.legend(titles, title='Track Legend', bbox_to_anchor=(1, 0.5), loc="center", fontsize='small')

    plt.axis('equal') 
    plt.title(f"{artist}'s top songs by daily streams", fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.tight_layout()
    plt.savefig('static/visualizations/artist_daily_pie.png')

    # create bar chart
    plt.figure(figsize=(12, 10))
    plt.bar(titles, daily_streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Titles')
    plt.ylabel('Streams')
    title = f"{artist}'s top songs by daily streams"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18) 
    plt.tight_layout()
    plt.savefig('./static/visualizations/artist_daily_bar.png')

# ---------------------------------------

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/artists', methods=['GET', 'POST'])
def artist_page():
    if request.method == 'POST':
        artist_name = request.form['artist_name']
        plot_artist_album_chart(artist_name)
        plot_artist_songs_chart(artist_name)
        build_artist_top_songs_by_daily_streams(artist_name)
        return redirect(url_for('visualizations', artist_name=artist_name))
    return render_template('artists.html')

@app.route('/visualizations/<artist_name>', methods=['GET'])
def visualizations(artist_name):
    # Perform data processing and visualization here based on the artist_name
    # For example, you can call a function that generates a chart
    # chart = artists_most_streamed_songs_bar_chart(artist_name)

    # Pass the artist_name and chart to the template
    return render_template('artists_visualizations.html', artist_name=artist_name)

@app.route('/songs', methods=['GET', 'POST'])
def song_page():
    if request.method == 'POST':
        song_name = request.form['song_name']
        # Perform visualization based on song_name using execute_query function
        # Example: result = execute_query("SELECT * FROM songs WHERE title=?", (song_name,))
        # Add your visualization logic here
        return render_template('songs', song_name=song_name)
    return render_template('songs.html')

@app.route('/albums', methods=['GET', 'POST'])
def album_page():
    if request.method == 'POST':
        album_name = request.form['album_name']
        # Perform visualization based on album_name using execute_query function
        # Example: result = execute_query("SELECT * FROM albums WHERE title=?", (album_name,))
        # Add your visualization logic here
        return render_template('albums', album_name=album_name)
    return render_template('albums.html')

if __name__ == '__main__':
    app.run(debug=True)
