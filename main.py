from pypresence import Presence
import os
import pafy
from win32gui import GetWindowText, GetForegroundWindow
import time
from utils.WindowUtil import getActiveProcessName
from dotenv import load_dotenv
from utils.getTab import BrowserWindow
from re import search
load_dotenv()


client_id = os.environ.get("clientid")
hoverText = os.environ.get("hoverText")
RPC = Presence(client_id,pipe=0)
RPC.connect()

timestamp = time.time()



while True:
    try:
        bw = BrowserWindow("Google Chrome")
        bwURL = bw.current_tab_url
        bwNoHttps = bwURL[8:]
        website = GetWindowText(GetForegroundWindow()).split()    
        window_name = getActiveProcessName()
        empty = " "
        stackoverflow = website[0] + " " + website[1]
        removeChrome = website[-2] + " " + website[-1]
    except:
        print("Error handler:")
        RPC.update(details="Relaxing", large_image="relax", large_text=hoverText, small_image="dnd",
                   small_text="Do not disturb",
                   buttons=[{"label": "Join Discord", "url": "https://discord.gg/dxVxWZejYG"}])
    if window_name == "chrome.exe":
        RPC.clear()
        if bwURL == "https://www.youtube.com":
           

            RPC.update(details="Browsing videos",state="On YouTube", large_image="youtube", large_text=hoverText,
                        small_image="dnd", buttons=[{"label": "Watch with me", "url": bwURL}])
        elif  search("https://www.youtube.com", bwURL):
            url = bwURL
            video = pafy.new(url)
            print(video)
            RPC.update(details="Watching",state=empty.join(website[:-5]), large_image="youtube", large_text=hoverText,
                        small_image="dnd", buttons=[{"label": "Watch with me", "url": bwURL}])
        else:

            RPC.update(details="Relaxing", large_image="relax", large_text=hoverText, small_image="dnd",
                    small_text="Do not disturb", buttons=[{"label": "Look with me", "url": bwURL}])
    else:
        print("Chrome was not detected")
        
     
 
     
     
    time.sleep(5)    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        # elif website[-4] == "Search":
        #     del website[-3:]
        #     final = " "

        #     RPC.update(details=final.join(website), state="Exploring the web", large_image="googlesearch",
        #                large_text=hoverText,
        #                small_image="dnd")
        # elif stackoverflow == "Stack Overflow":
        #     del website[-3:]
        #     final = " "



        #     RPC.update(details=final.join(website), state="Exploring",
        #                large_image="stackoverflow",
        #                large_text=hoverText,
        #                small_image="dnd")
        # elif removeChrome == "YouTube Music":

        #     del website[-3:]
        #     final = " "

        #     RPC.update(details=final.join(website), state="YouTube Music", large_image="youtubemusic",
        #                large_text=hoverText,
        #                small_image="dnd")


    # elif window_name == "pycharm64.exe":

    #     try:
    #         RPC.update(details="Working on \n" + str(website[0]),state="Editing "+ str(website[2]), large_image="pycharm", large_text=hoverText, small_image="online", start=timestamp)
    #     except:
    #         RPC.update(details="Browsing", large_image="pycharm", large_text=hoverText, small_image="online", start=timestamp)
    # else:
    #     RPC.update(details="Relaxing", large_image="relax", large_text=hoverText, small_image="dnd",
    #               small_text="Do not disturb", buttons=[{"label": "Join Discord", "url": "https://discord.gg/dxVxWZejYG"}])


    time.sleep(5)