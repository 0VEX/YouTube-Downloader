# youtube-downloader
# ----------------------------------------------------------------------------------------------------

# libraries

from tracemalloc import start
from click import option
from httpcore import stream
from numpy import choose
import pytube
from pytube import Playlist
from colorama import Fore

# the king

print("""
           +-----------------------------------------------------------------------------------------+
           |               ██╗   ██╗                ███████╗                ██╗  ██╗                 |
           |               ██║   ██║                ██╔════╝                ╚██╗██╔╝                 |
           |               ██║   ██║                █████╗                   ╚███╔╝                  |
           |               ╚██╗ ██╔╝                ██╔══╝                   ██╔██╗                  |
           |                ╚████╔╝                 ███████╗                ██╔╝ ██╗                 |
           |                 ╚═══╝                  ╚══════╝                ╚═╝  ╚═╝                 | 
           |            GIHUB : VEXDES1      INSTAGRAM : VEXDES1      DISCORD : V E X#5180           |                                                                        
           +-----------------------------------------------------------------------------------------+                                                                                       
                                                                                       """)


ans=True
while ans:
    print ("""
    [1].download video
    [2].download playlist
    [3].Exit the tool
    """)
    ans=input("[?]What would you like to do : ") 
    if ans=="1":
     print("\n[+] Welcome to youtube video downloader tool") 
     print("")          
     # asks the user to input the link

     link = input(f"[+]please enter the video url : ")
     print("")
     # asks the user what resolution 

     x = input(f"[+]please enter the resolution you want (144p)(240p)(360p)(480p)(720p)(1080p) : ")
     print("")

     # opens the link user inputed

     yt = pytube.YouTube(link)

     # gets the video resulution user inputed - x is the input

     stream = yt.streams.filter(res=x).first().download()

     # teeling user done downloading

     print("[+]Done downloading video , you can check it in the same path tool is opend")

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

      video.streams.filter(res=x).first().download() 


    elif ans=="3":
      print("\n[-]Thanks for using youtube downloader") 
      exit()
    elif ans !="":
      print("\n[-]Not Valid Choice Try again") 
