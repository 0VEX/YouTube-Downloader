# youtube-downloader
# ----------------------------------------------------------------------------------------------------

# libraries

from time import sleep, time
from email.mime import base
from hashlib import new
from time import sleep
from tracemalloc import start
from click import option
from httpcore import stream
from numpy import choose
import pytube
from pytube import Playlist , Channel , YouTube
from colorama import Fore
import os

# the king

print("""
         ██╗   ██╗████████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ 
         ╚██╗ ██╔╝╚══██╔══╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗
          ╚████╔╝    ██║       ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║
           ╚██╔╝     ██║       ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║
            ██║      ██║       ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝
            ╚═╝      ╚═╝       ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                     |- Programmed By : TheGreatVex -|                               
                                                                                       """)


ans=True
while ans:
    print ("""
----------------------------------------------------
    [1].download video
    [2].download playlist
    [3].download channel videos
    [4].Convert Youtube videos to mp3
    [5].Exit the tool
----------------------------------------------------
    """)
    ans=input("[?]What would you like to do : ") 
    if ans=="1":
     print("\n[+] Welcome to youtube video downloader tool") 
     print("")          
     # asks the user to input the link

     link = input(f"[+]please enter the video url : ")
     print("")
     # asks the user what resolution 

     x = input(f"[+]please enter the resolution you want (144p)(240p)(360p)... : ")
     print("")

     # opens the link user inputed

     yt = pytube.YouTube(link)

     # gets the video resulution user inputed - x is the input

     stream = yt.streams.filter(res=x , progressive=True).first().download()

     # teeling user done downloading

     print("[+]Done downloading video , you can check it in the same path tool is opend")
     time.sleep(5)

     # downloads the video with resulution chose in the same path tool is opend

     stream.download()


    elif ans=="2":
     print("\n[+] Welcome to youtube playlist downloader tool") 

     # asks the user to input the link

     link =input("[+]please enter the playlist url : ")

     # getting the resolution from user

     x = input(f"[+]please enter the resolution you want (144p)(240p)(360p)(480p)(720p)(1080p) : ")
     print("")

     # getting the playlist link

     p = Playlist(link)

     # priniting the the playlist is downloading

     print(f'[+]Downloading: {p.title}')

     # gettingthe first video in playlist

     for video in p.videos:

      # start downloadig

      video.streams.filter(res=x , progressive=True).first().download() 

    elif ans=="3":
     print("\n[+] Welcome to youtube channel videos downloader tool") 
     print("")
  
     # asks the user for channel url  

     c = input("[+]please enter channel url : ")
     print("")
     
     # asks the user what resolution he wants

     x = input(f"[+]please enter the resolution you want (144p)(240p)(360p)(480p)(720p)(1080p) : ")
     print("")

     # add the url inputed in c

     c = Channel(c)
     
     # print in the terminal that videos are downloading

     print(f"[+]Downloading videos by : {c.channel_name}")
    
     # getting the videos

     for video in c.videos:
           # downloading the video with choosen resolution

           video.streams.filter(res=x , progressive=True).first().download()
    
    elif ans=="4":
     print("\n[+]Welcome to youtube videos converter to mp3 tool") 
     print("")
     
      # asks the user to input the link

     link = input(f"[+]please enter the video url : ")
     print("")

     #add the link to the tool
 
     yt = YouTube(link)

     #
     
     try:
         print("\n[+]Converting...")
         video = yt.streams.filter(only_audio=True).first()
         out_file = video.download()

         base, ext =os.path.splitext(out_file)
         new_file = base + ".mp3"
         os.rename(out_file, new_file)
         print("\n[+]Successfully converting\n")
     except:
        print("\n[-]Somthing went wrong , please try again")    

    elif ans=="5":
      print("\n[-]Thanks for using youtube downloader") 
      exit()
    
    elif ans !="":
      print("\n[-]Not Valid Choice Try again") 
