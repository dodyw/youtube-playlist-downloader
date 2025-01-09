# YouTube Playlist Downloader

A simple CLI tool to download all videos from a YouTube playlist in the best available quality.

## Requirements

- Python 3.11+
- yt-dlp
- click

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

```bash
./download_playlist.py "PLAYLIST_URL"
```

Replace `PLAYLIST_URL` with the URL of the YouTube playlist you want to download.

Example:
```bash
./download_playlist.py "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

The script will:
- Download all videos in the best available quality
- Merge video and audio into MP4 format
- Show download progress for each video
- Skip any videos that can't be downloaded
- Save all videos in the `videos` folder (created automatically)

## Author

**Dody Rachmat W.**
- Website: [www.nicecoder.com](https://www.nicecoder.com)
- Email: dody@nicecoder.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
