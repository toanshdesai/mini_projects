from yt_dlp import YoutubeDL
from sys import argv

try:
    link = argv[1]
except IndexError:
    link = input("Enter the YouTube video link: ")

ydl_opts = {
    'quiet': True,
    'no_warnings': True,
    'outtmpl': '%(title)s.%(ext)s',
    'progress_hooks': [lambda d: print(f"\r{d['_percent_str']} of {d['_total_bytes_str']} at {d['_speed_str']}", end='') if d['status'] == 'downloading' else None],
}

print(f"Extracting URL: {link}")
with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link, download=True)
    print(f"\nDestination: {info['title']}.{info['ext']}")
print("Download complete!")
