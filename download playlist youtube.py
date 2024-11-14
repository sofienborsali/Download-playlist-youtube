import os
import yt_dlp

def download_playlist_to_mp3(playlist_url, download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
playlist_url = input("Enter the playlist URL: ")
# Example usage
download_folder = 'downloaded_mp3s'
download_playlist_to_mp3(playlist_url, download_folder)