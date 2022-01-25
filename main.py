from pytube import YouTube
from pytube import Playlist
from pathlib import Path
import platform
import os
import subprocess
import shutil

defaultLinuxPath = str(Path.home()) + '/Music' 
defaultWindowsPath = str(Path.home()) + '\\Music'

urlList = open('urllist.txt','r')


def clean(title):
    os.rename('test.mp3',title)
    os.remove('Download_Video')
    defaultPath = ''
    choice = input("Do you want to choose the destination directory for downloaded musics ?(y/n)")
    if choice == 'yes':
        defaultPath = input()
    elif platform.system() == "Linux":
        defaultPath = defaultLinuxPath
    else:
        defaultPath = defaultWindowsPath
    shutil.move(title,defaultPath)


def process(choice):
    length = 0
    if choice == "n":
        for url in urlList.readlines():
            videoObject = YouTube(url)
            print("Downloading: ",videoObject.title)
            filteredMP4 = videoObject.streams.filter(progressive = True, file_extension ="mp4")
            filteredMP4[0].download(filename="Download_Video")
            ffmpeg = (f'ffmpeg -i Download_Video test.mp3')
            subprocess.call(ffmpeg,shell=True)
            title = videoObject.title.replace("/",'')+".mp3"
            clean(title)
            length+=1
    else:
        playlist_link = input("Playlist link: ");
        playlist = Playlist(playlist_link)
        for video in playlist.videos:
            print("Downloading: ", video.title)
            if(len(video.title)<=90):
                video.streams.filter(progressive=True,file_extension="mp4")[0].download(filename="Download_Video")
                ffmpeg = (f'ffmpeg -i Download_Video test.mp3')
                subprocess.call(ffmpeg,shell=True)
                title = video.title.replace("/",'')+".mp3"
                #Cleaning and delete the downloaded video
                clean(title)
                length+=1
    print(f'Complete download {length} songs')

def main():
    choice = input("Do you want to download a playlist ?(y/n)")
    process(choice)

if __name__ == "__main__":
    main()
