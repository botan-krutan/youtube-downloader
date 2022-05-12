from tkinter import *
import yt_downloader

def empty_line():
    v = Label(window, text="    ")
    v.pack()

def download():
    if 'playlist' in inputtxt.get(1.0, "end-1c"):
        yt_downloader.download_playlist(inputtxt.get(1.0, "end-1c"), variable.get(), status)
    else: 
        yt_downloader.download_video(inputtxt.get(1.0, "end-1c"), variable.get(), status)   
window = Tk()

window.title("Youtube Downloader")
window.geometry('640x360')

txt = Label(window, text="Youtube Downloader")
txt.pack()

empty_line()

variable = StringVar(window)
variable.set("mp4") # default value

opt = OptionMenu(window, variable, "mp3", "mp4")
opt.pack()

empty_line()

inputtxt = Text(window, height=3, width=50)
inputtxt.pack()

empty_line()

subm = Button(window, text="Download", command=download)
subm.pack()

empty_line()

status = Label(window, text="    ")
status.pack()

empty_line()

q = Button(window, text="Quit", command=window.destroy)
q.pack()

window.mainloop()
