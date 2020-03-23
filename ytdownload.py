#!/usr/bin/python3

import pytube
import math
from pytube import YouTube
import sys, os, optparse

dstream = []

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

# def show_progress_bar(stream: Stream, chunk: bytes, bytes_remaining: int):
#     return  # do work

# def progress_function(stream, chunk, file_handle, bytes_remaining):
#     print(round((1-bytes_remaining/dstream[0].filesize)*100, 3), '% done...')

# Function to download Video

def videod(video):
    vidres = [144,360,480,720,1080] # Resolutions to be checked
    availres = []
    checkres = []
    # Filter mp4 videos and get the available resolutions!
    for res in vidres:
        composeres = str(res) + "p"
        checkres = video.streams.filter(only_video=True, subtype='mp4', resolution=composeres)
        checkreslen = len(checkres)
        if checkreslen != 0:
            availres.append(res) # This list contains all the abailable resolution
    print("\n Available resolutions for download are: ")
    i = 1
    
    # Print the available resolutions!
    for res in availres:
        print(str(i) + ". " + str(availres[i-1]) + 'p')
        i = i+1
    getinput = int(input(": > "))
    
    # Narrowing down to the one stream to be downloaded!
    if getinput <= int(len(availres)):
        dstream = video.streams.filter(only_video=True, subtype='mp4', resolution=str(availres[getinput-1]) + 'p')
        fsize = dstream[0].filesize
        print("> Video Title: " + video.title)
        print("> Resolution: " + str(availres[getinput-1]) + 'p')
        print("> File Size: " + str(convert_size(fsize)))
        print("Downloading...\n")
        dstream[0].download() # Downloading selected Video stream
    else:
        print("Please select correct option")

# Function to Download Audio

def audiod(video):
    audres = [50,70,128,160] # Bit Rates to be checked
    availres = []
    checkres = []
    
    # Filter audio streams and get the available bit rates!
    for res in audres:
        composeres = str(res) + "kbps"
        checkres = video.streams.filter(only_audio=True, abr=composeres)
        checkreslen = len(checkres)
        if checkreslen != 0:
            availres.append(res) # This list contains all the abailable Bit Rates
    print("\n Available resolutions for download are: ")
    i = 1

    # Print available resolutions
    for res in availres:
        print(str(i) + ". " + str(availres[i-1]) + ' kbps')
        i = i+1
    getinput = int(input(": > "))

    # Narrowing down to the one stream to be downloaded!
    if getinput <= int(len(availres)):
        dstream = video.streams.filter(only_audio=True, abr=str(availres[getinput-1]) + 'kbps')
        fsize = dstream[0].filesize
        print("> Video Title: " + video.title)
        print("> Resolution: " + str(availres[getinput-1]) + 'kbps')
        print("> File Size: " + str(convert_size(fsize)))
        print("Downloading...\n")
        dstream[0].download() # Downloading selected audio stream

def main():
    link = input("\n Please enter the youtube link to download:> ")
    # Video Info
    # video = YouTube(link, on_progress_callback=progress_function) 
    try:
        video = YouTube(link) 
    except:
        print("Error! Please Check: \n [!] Internet Connection \n [!] The URL is a YouTube URL \n Try Again!")
        redo = main()
        
    print("\n The video you are trying to download is: \n " + video.title)
    aud = video.streams.filter(only_audio=True).order_by('abr')
    vid = video.streams.filter(only_video=True, subtype='mp4').order_by('resolution')
    
    dselect = input("\n What would you like to download? \n 1. Video? (" + str(len(vid)-1) + " options available) \n 2. Audio? (" + str(len(aud)-1) + " options available) \n : > ")
    if dselect == '1':
        videod(video)
    elif dselect == '2':
        audiod(video)
    else:
        print("\n Please select correct option!")
        sys.exit(0)

if __name__ == "__main__":
    main()
