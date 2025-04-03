import os
from dotenv import load_dotenv
import yt_dlp
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

# Spotify API authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri='http://localhost:8888/callback',
                                               scope=["playlist-read-private", "user-library-read"]))


# Function to fetch tracks from a Spotify playlist
def get_tracks_from_spotify(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    track_info = []

    for item in tracks:
        track_name = item['track']['name']
        artist_name = item['track']['artists'][0]['name']
        track_info.append((track_name, artist_name))

    return track_info


# Function to download a song from YouTube
def download_song_from_youtube(song_name, artist):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best audio quality
        'outtmpl': f'C:/Users/artur/Videos/Music/{song_name} - {artist}.%(ext)s',  # Save location
        'noplaylist': True,  # Disable playlist downloads
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{song_name} {artist}"])  # Search and download the song from YouTube


# Example usage:
playlist_id = "5lTaxK0R9LowRm9IBsrvHC"  # Your playlist ID

# Fetch tracks from the Spotify playlist
tracks = get_tracks_from_spotify(playlist_id)

# Download each song using YouTube
for track in tracks:
    track_name, artist_name = track
    print(f"Downloading: {track_name} - {artist_name}")
    download_song_from_youtube(track_name, artist_name)
