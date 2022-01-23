from pytube import YouTube
from pytube import Playlist
from pathlib import Path
import os
import subprocess
import shutil


urlList = open('urllist.txt','r')

length = 0

choice = input("Do you want to download a playlist ?(y/n)")

if choice == "n":
    for url in urlList.readlines():
        videoObject = YouTube(url)
        print("Downloading: ",videoObject.title)
        filteredMP4 = videoObject.streams.filter(progressive = True, file_extension ="mp4")
        filteredMP4[0].download(filename="Download_Video")
        ffmpeg = (f'ffmpeg -i Download_Video test.mp3')
        subprocess.call(ffmpeg,shell=True)
        title = videoObject.title.replace("/",'')+".mp3"
        
        #Cleaning and delete the downloaded video
        os.rename('test.mp3',title)
        os.remove('Download_Video')
        shutil.move(title,'/home/nguyen/Music/')
        length+=1
else:
    playlist_link = input("Playlist link: ");
    playlist = Playlist(playlist_link)
    for video in playlist.videos:
        print("Downloading: ", video.title)
        if(len(video.title)<=90):
            title = video.title.replace("/",'')+".mp3"
            video.streams.filter(progressive=True,file_extension="mp4")[0].download(filename="Download_Video")
            ffmpeg = (f'ffmpeg -i Download_Video test.mp3')
            subprocess.call(ffmpeg,shell=True)
            #Cleaning and delete the downloaded video
            os.rename('test.mp3',title)
            os.remove('Download_Video')
            shutil.move(title,'/home/nguyen/Music/')
            length+=1

print(f'Complete download {length} songs')
