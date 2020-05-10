from pytube import YouTube #get video from youtube
from tkinter import * #create window
from tkinter import filedialog #Create window that asks where to download file to 
import pyperclip #copy-paste
import os
from pytube.helpers import safe_filename #gets rid of characters that would not work in title of video
import time #wait
from moviepy.editor import * #edit video and audio
import pathlib


root = Tk()
root.title("Youtube Video Downloader")
root.geometry("500x200")

#Copy and Paste Class

class StationaryFunctions:
    def __init__(self, text):
        self.text = text
        self.create_binding_keys()
        # self.binding_functions_config()
        self.join_function_with_main_stream()
    
    def join_function_with_main_stream(self):
        self.text.storeobj['Copy'] = self.copy
        self.text.storeobj['Paste'] = self.paste
        self.text.storeobj['SelectAll'] = self.select_all
        self.text.storeobj['DeselectAll'] = self.deselect_all
        return
   
    
    def copy(self, event):
        self.text.event_generate("&lt;&lt;Copy>>")
        return
    
    def paste(self, event):
        self.text.event_generate('&lt;&lt;Cut>>')
        return
    
    def create_binding_keys(self):
        for key in ["&lt;Control-a>", "&lt; Control-A>"]:
            self.text.master.bind(key, self.select_all)
        for key in ["&lt;Button-1>", "&lt;Return>"]:
            self.text.master.bind(key, self.deselect_all)
    
    def select_all(self, event):
        self.text.tag_remove("sel", "1.0", "end")
        return
    
    def deselect_all(self, event):
        self.text.tag_remove("sel", "1.0", "end")
        return 

input1 = StringVar()

newDirectory = ""
def getDirectory():
    global directory
    directory = filedialog.askdirectory()
    newDirectory = []
    for i in range(len(str(directory))):
        if directory[i] == "\\":
            newDirectory.append("\\")
        else:
            newDirectory.append(directory[i])

def getEntry():
    yt = YouTube(entryBox.get())
    #do just audio
    name = (safe_filename(yt.title))
    # stream = yt.streams.filter(only_audio = True).first()
    stream = yt.streams.first()
    stream.download(filename=name)
    name1 = name + ".mp4"
    path = str(newDirectory) + str(name1)
    video = VideoFileClip(path)
    name2 = name + ".mp3"
    path2 = str(newDirectory) + str(name2)
    video.audio.write_audiofile(path2)
    time.sleep(1)
    name3 = str(newDirectory) + str(name1)
    pathlib.Path.unlink(name3)
    os.remove(path)

    print("Downloaded Audio")



def downloadVideo():
    yt = YouTube(entryBox.get())
    name = (safe_filename(yt.title))
    yt.streams.first().download(filename=name)
    print("Downloaded Video")

#Clear out box when you click on it
def clear_search(event):
    entryBox.delete(0,END)


#Make box and put text in, then clear it when clicked
entryBox = Entry(width = 45)
entryBox.insert(0, "Paste Youtube link in here")
if len(entryBox.get()) == 26:
    entryBox.bind("<Button-1>", clear_search)

#buttons that let you either download audio or picture too
entryButton = Button(text = "Click to download the audio", command = getEntry)
entryButtonVideo = Button(text = "Click to download the video", command = downloadVideo)
directoryButton = Button(text = "click to select where the file is downloaded", command = getDirectory)

#Copy-Paste attempt 2
for key in ["&lt;Control-C>","&lt; Control-C>"]:
    pyperclip.copy(entryBox.get())

for key in ["&lt;Control-C>", "&lt; Control-C>"]:
    entryButton.text = pyperclip.paste()

#needed for copy paste
entryBox.storeobj = {}
StationaryFunctions(entryBox)

#place all widgets on tkinter window
entryBox.grid(row = 0,column = 1)
entryButton.grid(row = 2,column = 1)
entryButtonVideo.grid(row = 3, column = 1)
directoryButton.grid(row = 1, column = 1)

root.mainloop()
