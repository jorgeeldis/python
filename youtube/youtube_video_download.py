from pytube import YouTube
import os

def download_youyube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

link = input()
download_youyube(link,".")