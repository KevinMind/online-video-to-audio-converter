from __future__ import unicode_literals
import youtube_dl
import json

options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,  # only keep the audio
  'audioformat' : "mp3",  # convert to mp3
  'outtmpl': 'file{}.mp3'.format(id),    # name the file the ID of the video
  'noplaylist' : True,    # only download single song, not playlist
}

ydl = youtube_dl.YoutubeDL(options)


def download(url):
    ydl.download([url])

def meta_data(url):
    r = ydl.extract_info(url, download=False)
    for key in r:
        print(key)
        print(r[key])
        print('\n\n\n\n\n\n')


url = 'https://www.youtube.com/watch?v=ew3xLp5OWJg'

download(url)
