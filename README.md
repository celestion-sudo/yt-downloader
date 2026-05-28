# ytloader

[![CI](https://github.com/celestion-sudo/yt-downloader/actions/workflows/ci.yml/badge.svg)](https://github.com/celestion-sudo/yt-downloader/actions/workflows/ci.yml)

A small Linux command-line downloader for YouTube so that users can download video. It saves files to the default Downloads folder and can automatically use a standalone `yt-dlp` binary if Python package installation is unavailable.

## Requirements

- Python 3.8+
- Network access for the fallback `yt-dlp` binary download when needed

## Installation

Clone the repository:

```bash
git clone https://github.com/celestion-sudo/yt-downloader.git
cd yt-downloader
```

Install dependencies and package entrypoints:

```bash
python3 -m pip install -e .
```

If you do not have `python3-venv` installed, install into your local user site instead:

```bash
python3 -m pip install --user -e .
```

If you prefer not to install, you can run the tool directly from source:

```bash
./ytloader.sh "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Run from source

From the repository root, use either of these:

```bash
python3 -m ytloader "https://www.youtube.com/watch?v=VIDEO_ID"
```

or:

```bash
python3 -m ytloader.ytloader "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Run the wrapper script

Make the wrapper executable and use it directly from the repo root:

```bash
chmod +x ytloader.sh
./ytloader.sh "https://www.youtube.com/watch?v=VIDEO_ID"
```

After installation, the `ytloader` CLI is available globally:

```bash
ytloader "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Usage

- Run and paste a URL when prompted:

```bash
python3 -m ytloader
```

- Download directly with a URL:

```bash
python3 -m ytloader "https://www.youtube.com/watch?v=VIDEO_ID"
```

- Download audio only:

```bash
python3 -m ytloader --audio "https://www.youtube.com/watch?v=VIDEO_ID"
```

- Save to a custom folder:

```bash
python3 -m ytloader -o ~/MyDownloads "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Notes

- If Python package installation is blocked, the tool will try to download a standalone `yt-dlp` binary to `~/.local/bin/yt-dlp`.
- The default download folder is `Downloads` or the value of `XDG_DOWNLOAD_DIR`.
- If YouTube extraction warns about a JavaScript runtime, install Node or Deno for better compatibility.

## Example output

```
Running yt-dlp binary...
[youtube] Video Title: Downloading webpage
Downloading: 100.0% ETA: 0s Speed: 1.2MiB/s
Download finished, processing...
```
