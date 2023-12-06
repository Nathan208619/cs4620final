from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.cm as cm

app = Flask(__name__)

def check_if_artist_exists(artist):
    conn = sqlite3.connect("music.db")
    query = "SELECT streams_id FROM most_streams, most_streamed_artist WHERE most_streams.artist_id = most_streamed_artist.artist_id AND artist='" + artist + "' AND streams_id < 2469"
    data = query_the_database(conn, query)
    query = "SELECT album FROM most_streamed_album JOIN most_streamed_artist ON most_streamed_album.artist_id = most_streamed_artist.artist_id WHERE artist='" + artist + "'"
    data2 = query_the_database(conn, query)
    # query = "SELECT streams FROM most_streamed_artist WHERE artist='" + artist + "'"
    # data3 = query_the_database(conn, query)
    conn.close()
    
    if len(data) == 0:
        print(f"No data found for the artist: {artist}")
        return False
    if len(data2) == 0:
        print(f"No data found for the artist: {artist}")
        return False
    print(f"Data found for the artist: {artist}")
    return True
    

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
def plot_artist_songs_chart(artist):

    # query the database
    conn = sqlite3.connect("music.db")
    query = "SELECT title, total_streams FROM most_streams JOIN most_streamed_artist ON most_streams.artist_id = most_streamed_artist.artist_id WHERE artist='" + artist + "' AND total_streams != 0 ORDER BY total_streams DESC"
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
    plt.savefig('./static/visualizations/artist_songs.png')

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
    plt.savefig('./static/visualizations/artist_albums.png')


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
    plt.savefig('static/visualizations/artist_daily_pie.png')

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
    plt.savefig('./static/visualizations/artist_daily_bar.png')

# ---------------------------------------

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/artists', methods=['GET', 'POST'])
def artist_page():
    if request.method == 'POST':
        artist_name = request.form['artist_name'].lower()
        names = artist_name.split(" ")
        names = [name.capitalize() for name in names]
        artist_name = " ".join(names)
        if check_if_artist_exists(artist_name) == False:
            return render_template('error.html')
        plot_artist_album_chart(artist_name)
        plot_artist_songs_chart(artist_name)
        build_artist_top_songs_by_daily_streams(artist_name)
        return redirect(url_for('visualizations', artist_name=artist_name))
    return render_template('artists.html')

@app.route('/visualizations/<artist_name>', methods=['GET'])
def visualizations(artist_name):
    return render_template('artists_visualizations.html', artist_name=artist_name)

@app.route('/songs', methods=['GET'])
def song_page():
    return render_template('songs.html')

@app.route('/albums', methods=['GET'])
def album_page():
    return render_template('artist_comparisons.html')

if __name__ == '__main__':
    app.run(debug=True)
