#!/usr/bin/env python3

import click
from yt_dlp import YoutubeDL
import sys
import os

def create_ydl_opts():
    # Create videos directory if it doesn't exist
    os.makedirs('videos', exist_ok=True)
    
    return {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Best quality
        'merge_output_format': 'mp4',  # Merge video and audio into mp4
        'ignoreerrors': True,  # Skip videos that can't be downloaded
        'progress_hooks': [progress_hook],  # Progress callback
        'outtmpl': 'videos/%(title)s.%(ext)s',  # Save in videos folder
    }

def progress_hook(d):
    if d['status'] == 'downloading':
        # Calculate progress percentage
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
        if total_bytes > 0:
            downloaded = d.get('downloaded_bytes', 0)
            progress = (downloaded / total_bytes) * 100
            sys.stdout.write(f"\rDownloading {d['filename']}: {progress:.1f}%")
            sys.stdout.flush()
    elif d['status'] == 'finished':
        print(f"\nFinished downloading {d['filename']}")

@click.command()
@click.argument('playlist_url')
def download_playlist(playlist_url):
    """
    Download all videos from a YouTube playlist in the best available quality.
    
    PLAYLIST_URL: The URL of the YouTube playlist to download
    """
    try:
        print(f"Starting download of playlist: {playlist_url}")
        with YoutubeDL(create_ydl_opts()) as ydl:
            ydl.download([playlist_url])
        print("\nPlaylist download completed successfully!")
        
    except Exception as e:
        print(f"\nError downloading playlist: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    download_playlist()
