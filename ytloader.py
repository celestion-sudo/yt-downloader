#!/usr/bin/env python3
import argparse
import os
import sys
from pathlib import Path

import shutil
import stat
import subprocess
import urllib.request

yt_dlp = None
USE_BINARY = False
try:
    import yt_dlp
except Exception:
    yt_dlp = None
    USE_BINARY = True


def get_default_download_dir():
    xdg = os.environ.get("XDG_DOWNLOAD_DIR")
    if xdg:
        return os.path.expanduser(xdg)
    home_dl = Path.home() / "Downloads"
    return str(home_dl)


def progress_hook(d):
    if d['status'] == 'downloading':
        speed = d.get('speed')
        eta = d.get('eta')
        downloaded = d.get('downloaded_bytes')
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        percent = d.get('_percent_str', '').strip()
        print(f"Downloading: {percent} ETA: {eta}s Speed: {speed}", end='\r')
    elif d['status'] == 'finished':
        print("\nDownload finished, processing...\n")


def ensure_yt_dlp_binary():
    """Ensure a `yt-dlp` binary is available; download to ~/.local/bin if needed."""
    bin_name = 'yt-dlp'
    # check PATH first
    path = shutil.which(bin_name)
    if path:
        return path

    # fallback location
    local_bin = Path.home() / '.local' / 'bin'
    local_bin.mkdir(parents=True, exist_ok=True)
    dest = local_bin / bin_name
    if dest.exists() and os.access(dest, os.X_OK):
        return str(dest)

    # try to download the official release binary
    url = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp'
    try:
        print(f"Downloading yt-dlp to {dest}...")
        with urllib.request.urlopen(url) as resp, open(dest, 'wb') as out:
            out.write(resp.read())
        dest.chmod(dest.stat().st_mode | stat.S_IEXEC)
        print('yt-dlp downloaded and made executable')
        return str(dest)
    except Exception as e:
        print(f"Could not download yt-dlp binary: {e}")
        return None


def normalize_url_input(raw):
    if not raw:
        return None
    return raw.strip()


def main():
    p = argparse.ArgumentParser(description="Simple yt downloader CLI that saves to Downloads folder by default")
    p.add_argument('url', nargs='?', help='Video or playlist URL to download')
    p.add_argument('-o', '--output', help='Output directory (default: Downloads)')
    p.add_argument('--audio', action='store_true', help='Extract audio only')
    args = p.parse_args()

    url = args.url
    # If no URL provided and stdin is not a tty, try reading from stdin (pipe)
    if not url and not sys.stdin.isatty():
        url = sys.stdin.read().strip()

    # If still no URL, prompt the user to paste
    if not url:
        try:
            raw = input('Paste video URL and press Enter: ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nNo URL provided, exiting.')
            sys.exit(1)
        url = normalize_url_input(raw)

    if not url:
        print('No URL provided, exiting.')
        sys.exit(1)

    outdir = args.output or get_default_download_dir()
    outdir = os.path.expanduser(outdir)
    Path(outdir).mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(outdir, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'noprogress': False,
    }

    if args.audio:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })

    if yt_dlp is not None:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"Download failed: {e}")
            sys.exit(1)
    else:
        binpath = ensure_yt_dlp_binary()
        if not binpath:
            print("yt-dlp is required but could not be installed or downloaded.\nInstall with 'python3 -m pip install yt-dlp' or enable network to allow auto-download.")
            sys.exit(1)

        # build command for CLI
        outtmpl = os.path.join(outdir, '%(title)s.%(ext)s')
        cmd = [binpath, '-o', outtmpl]
        if args.audio:
            cmd += ['-f', 'bestaudio', '-x', '--audio-format', 'mp3', '--audio-quality', '0']
        cmd += [url]

        try:
            print('Running yt-dlp binary...')
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            # stream output
            for line in proc.stdout:
                print(line, end='')
            proc.wait()
            if proc.returncode != 0:
                print(f"yt-dlp exited with code {proc.returncode}")
                sys.exit(proc.returncode)
        except Exception as e:
            print(f"Failed to run yt-dlp: {e}")
            sys.exit(1)


if __name__ == '__main__':
    main()
