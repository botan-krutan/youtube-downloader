import pytube
import os
from moviepy.editor import *
import getpass

MUSIC_FOLDER = "C:\\Users\\" + getpass.getuser() + "\\Music\\"
VIDEO_FOLDER = "C:\\Users\\" + getpass.getuser() + "\\Videos\\"

def download_video(url: str, video: str, status):

    if video == "mp4": video = True
    else: video = False

    #getting streams and downloading the video
    yt = pytube.YouTube(url)
    if video: yt = yt.streams.get_highest_resolution()
    else: yt = yt.streams.get_lowest_resolution()
    yt.download(VIDEO_FOLDER)

    if video is False:
        #removing unwanted symbols from the file name
        symbols = ["/", ".", "\\", "|", "?", "*", ":", "<", ">", '"', "'"] 
        title = yt.title
        for i in symbols:
            title = title.replace(i, "")
        download_path = VIDEO_FOLDER + title + '.mp4'

        #converting to mp3 and closing the video file
        vid = VideoFileClip(download_path)
        vid.audio.write_audiofile(MUSIC_FOLDER + title + '.mp3')
        vid.close()

        #deleting the mp4 and sucess messages
        os.remove(download_path)
        status.config(text="Done! Moved " + title +".mp3" + " to Music!")
    else: 
        status.config(text="Done! Moved " + title +".mp4" + " to Videos!")



def download_playlist(url: str, video:str, status):
    #getting the playlist and looping through video url's
    p = pytube.Playlist(url)
    for vid_url in p.video_urls:
        download_video(vid_url, video, status)