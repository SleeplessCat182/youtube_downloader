# Youtube Downloader 

The script exists with a purpose of downloading multiple videos from youtube and store in a specific folder. Feel free to edit the script to satisfy your use.
I can not do this without the help of pytube package, please check their github also: https://github.com/pytube/pytube

Currently, the script only supports downloading mp3 files ( I have converted from mp4 to mp3 since pytube don't support that directly )

## Dependecies
1. [python](https://www.python.org/)
2. [ffmpeg](https://www.ffmpeg.org/)
3. [pytube](https://github.com/pytube/pytube)

To install pytube, open your terminal and use the following command. Remember to install ffmpeg, it is very important to convert video (mp4 format) to mp3
```python -m pip install pytube```

## Installation
1. clone the repo
### For different videos
2. Simply paste the video's url in the urllist.txt 
Note: Remember to paste each link on new lines
### For a playlist
2. Simply choose 'y' when running a script and paste the playlist link

### To do list
- [X] Fix the long name error (The script will skip any song whose name are longer than 90 characters, this look likes to be the limitation of the OS)
- [X] Allow to change the destination directory without modifying the script itself 
- [ ] GUI
- [ ] Implement error handling 
- [ ] Refactor the code
- [ ] More options when download files

