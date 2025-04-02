import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Завантаження конфігурацій з .env
load_dotenv()

# Ініціалізація API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                                client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                                                redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                                                scope="user-library-read"))

# Отримання списку збережених пісень
def get_saved_tracks():
    results = sp.current_user_saved_tracks()
    songs = []
    for idx, item in enumerate(results['items']):
        track = item['track']
        songs.append({
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "url": track['external_urls']['spotify']
        })
    return songs

if __name__ == "__main__":
    saved_songs = get_saved_tracks()
    for song in saved_songs:
        print(f"Song: {song['name']}, Artist: {song['artist']}, URL: {song['url']}")
