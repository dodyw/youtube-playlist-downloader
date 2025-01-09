# YouTube Playlist Downloader

A simple CLI tool to download videos or audio from YouTube playlists in the best available quality.

## Requirements

- Python 3.6+
- yt-dlp
- click

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Download Videos

```bash
./download_playlist.py "PLAYLIST_URL"
```

This will:
- Download all videos in the best available quality
- Merge video and audio into MP4 format
- Show download progress for each video
- Skip any videos that can't be downloaded
- Save all videos in the `output/mp4` folder (created automatically)

### Download Audio Only (MP3)

```bash
./download_playlist_audio.py "PLAYLIST_URL"
```

This will:
- Extract the best quality audio from each video
- Convert to MP3 format (320kbps quality)
- Show download progress for each audio file
- Skip any videos that can't be downloaded
- Save all audio files in the `output/mp3` folder (created automatically)

## Output Structure

```
output/
├── mp3/  # Contains downloaded MP3 audio files
└── mp4/  # Contains downloaded MP4 video files
```

## Author

**Dody Rachmat W.**
- Website: [www.nicecoder.com](https://www.nicecoder.com)
- Email: dody@nicecoder.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
