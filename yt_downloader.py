import yt_dlp

def download_song_from_youtube(song_name, artist):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best audio
        'postprocessors': [{
            'key': 'FFmpegAudioConvertor',  # Correct postprocessor
            'preferredcodec': 'mp3',  # Convert to mp3
            'preferredquality': '192',  # Quality of mp3
        }],
        'postprocessor_args': [
            '-ar', '44100',  # Optional: setting the audio sample rate
            '-ac', '2'  # Optional: setting the number of audio channels
        ],
        'outtmpl': f'./downloads/{song_name} - {artist}.%(ext)s',  # Save path
        'noplaylist': True,  # Disable playlist download if there's one
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{song_name} {artist}"])  # Search for the song on YouTube

# Example call
download_song_from_youtube("Song Name", "Artist Name")
