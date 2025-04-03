# Spotify Playlist Downloader

## Overview
This Python script allows users to fetch tracks from a Spotify playlist and download their corresponding audio from YouTube. The program uses the Spotify Web API to retrieve track details and `yt-dlp` to search and download the best available audio.

## Features
- Fetches tracks from a given Spotify playlist
- Searches for the corresponding song on YouTube
- Downloads the best quality audio file available
- Saves the files in a specified directory

## Requirements
Ensure you have the following installed:
- Python 3.8+
- `yt-dlp`
- `spotipy`

You can install the required packages using:
```sh
pip install yt-dlp spotipy python-dotenv
```

## Setup
1. **Create a `.env` file** in the project directory and add your Spotify API credentials:
   ```sh
   SPOTIPY_CLIENT_ID='your_client_id'
   SPOTIPY_CLIENT_SECRET='your_client_secret'
   SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
   ```
2. **Ensure `.env` is ignored by Git** by adding it to `.gitignore`:
   ```sh
   .env
   ```
3. **Run the script**:
   ```sh
   python script.py
   ```

## Usage
- Replace `playlist_id` in the script with your desired Spotify playlist ID.
- The downloaded audio files will be saved in `C:/Users/artur/Videos/Music/` (you can change the path in the script).

## License
This project is open-source and available under the MIT License.

