# ytloader

[![CI](https://github.com/celestion-sudo/yt-downloader/actions/workflows/ci.yml/badge.svg)](https://github.com/celestion-sudo/yt-downloader/actions/workflows/ci.yml)

A small Linux command-line downloader for YouTube and other supported sites. It saves files to the default Downloads folder and can automatically use a standalone `yt-dlp` binary if Python package installation is unavailable.

## Requirements

- Python 3.8+
- Network access for the fallback `yt-dlp` binary download when needed

## Installation

Run the downloader directly from the project folder:

```bash
python3 ytloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

To install the wrapper for easier use:

```bash
chmod +x ytloader
sudo mv ytloader /usr/local/bin/ytloader
```

If you want an isolated Python environment for development, use a virtualenv:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Try locally first

From the repository folder:

```bash
cd ~/Desktop/ytloader
python3 ytloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Or run as a module from the parent folder:

```bash
cd ~/Desktop
python3 -m ytloader.ytloader "https://www.youtube.com/watch?v=VIDEO_ID"
```

Check help output:

```bash
python3 -m ytloader.ytloader --help
```

## Usage

- Run and paste a URL when prompted:

```bash
python3 ytloader.py
```

- Download directly with a URL:

```bash
python3 ytloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

- Download audio only:

```bash
python3 ytloader.py --audio "https://www.youtube.com/watch?v=VIDEO_ID"
```

- Save to a custom folder:

```bash
python3 ytloader.py -o ~/MyDownloads "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Notes

- If Python package installation is blocked, the script will try to download a standalone `yt-dlp` binary to `~/.local/bin/yt-dlp`.
- The default download folder is `Downloads` or the value of `XDG_DOWNLOAD_DIR`.
- If YouTube extraction warns about a JavaScript runtime, install Node or Deno for better compatibility.

## Example output

```
Running yt-dlp binary...
[youtube] Video Title: Downloading webpage
Downloading: 100.0% ETA: 0s Speed: 1.2MiB/s
Download finished, processing...
```
