# ytloader

[![CI](https://github.com/celestion-sudo/yt-downloader/actions/workflows/ci.yml/badge.svg)](https://github.com/celestion-sudo/yt-downloader/actions/workflows/ci.yml)

A tiny command-line YouTube downloader for Linux that makes downloading videos fast and easy. It saves downloads to your `Downloads` folder by default and can automatically fall back to the standalone `yt-dlp` binary when Python package installation is blocked.

## Requirements

- Python 3.8+
- Network access to download the `yt-dlp` binary if the Python package is not installed.

## Installation

1. Create a virtualenv (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Make the wrapper executable (optional):

```bash
chmod +x ytloader
sudo mv ytloader /usr/local/bin/ytloader
```

## Test locally before deployment

From the repository folder:

```bash
cd ~/Desktop/ytloader
python3 ytloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

If you want to run the package as a module, use the parent folder:

```bash
cd ~/Desktop
python3 -m ytloader.ytloader "https://www.youtube.com/watch?v=VIDEO_ID"
```

To verify help output:

```bash
python3 -m ytloader.ytloader --help
```

## Usage

- Run and paste a URL when prompted:

```bash
python3 ytloader.py
# Paste the link and press Enter
```

- Pass a URL directly:

```bash
python3 ytloader.py "https://www.youtube.com/watch?v=..."
```

- Download audio-only:

```bash
python3 ytloader.py --audio "<url>"
```

- Specify an output directory:

```bash
python3 ytloader.py -o ~/MyDownloads "<url>"
```

Files will be saved to your `Downloads` directory by default.

> Note: If you cannot install `yt-dlp` into Python because your system blocks package installs, this script will try to download the standalone `yt-dlp` binary to `~/.local/bin/yt-dlp` and use it automatically.
>
> If you run into `python3 -m ytloader.ytloader` issues from inside the `ytloader/` folder, change to the parent folder (`cd ~/Desktop`) before running it.

## Quick sample

Run a direct download:

```bash
python3 -m ytloader.ytloader "https://www.youtube.com/watch?v=VIDEO_ID"
```

Or run and paste a link when prompted:

```bash
python3 ytloader.py
# Paste the link and press Enter
```

Sample output (successful download):

```
Running yt-dlp binary...
[youtube] Video Title: Downloading webpage
Downloading: 100.0% ETA: 0s Speed: 1.2MiB/s
Download finished, processing...
```

## Common troubleshooting

- If `python3 -m venv .venv` fails, install the system venv package:

```bash
sudo apt install python3-venv
```

- If `yt-dlp` is missing, the script will use a downloaded binary automatically.
- If YouTube extraction warns about a JavaScript runtime, install Node or Deno for better compatibility.

Notes:

- If the Python package `yt-dlp` is not installed and you cannot create a virtual environment, the script will try to download the standalone `yt-dlp` binary to `~/.local/bin` and use it automatically.
