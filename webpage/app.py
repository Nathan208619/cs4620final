from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def execute_query(query, params=None):
    try:
        conn = sqlite3.connect("music.db")
        c = conn.cursor()
        c.execute(query, params)
        result = c.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        print(e)
        return []

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/artists', methods=['GET', 'POST'])
def artist_page():
    if request.method == 'POST':
        artist_name = request.form['artist_name']
        print(artist_name)
        # Perform visualization based on artist_name using execute_query function
        # Example: result = execute_query("SELECT * FROM artists WHERE name=?", (artist_name,))
        # Add your visualization logic here
        return render_template('artists.html', artist_name=artist_name)
    return render_template('artists.html')

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
