
from pytube import YouTube
import os
from moviepy.editor import *
import getpass

MUSIC_FOLDER = "C:\\Users\\" + getpass.getuser() + "\\Music\\"
VIDEO_FOLDER = "C:\\Users\\" + getpass.getuser() + "\\Videos\\"

def download_video(url: str, video: bool, status):

    if video == "mp4": video = True
    else: video = False
    yt = YouTube(url)
    if video: yt = yt.streams.get_highest_resolution()
    else: yt = yt.streams.get_lowest_resolution()
    yt.download(VIDEO_FOLDER)
    if video is False: 
        download_path = VIDEO_FOLDER + yt.title.replace("'", "") + '.mp4'
        # print(VIDEO_FOLDER + yt.title + '.mp4')
        vid = VideoFileClip(download_path)
        vid.audio.write_audiofile(MUSIC_FOLDER + yt.title + '.mp3')
        # os.unlink(VIDEO_FOLDER + yt.title + '.mp4')
        vid.close() 
        os.remove(download_path)
        status.config(text="Done! Moved " + yt.title +".mp3" + " to Music!")
    else: status.config(text="Done! Moved " + yt.title +".mp4" + " to Videos!")

