from pypresence import Presence
import os
from win32gui import GetWindowText, GetForegroundWindow
import time
from utils.WindowUtil import getActiveProcessName
from dotenv import load_dotenv
load_dotenv()


client_id = os.environ.get("clientid")
hoverText = os.environ.get("hoverText")

RPC = Presence(client_id,pipe=0)
RPC.connect()

timestamp = time.time()



while True:
    try:
        website = GetWindowText(GetForegroundWindow()).split()
        window_name = getActiveProcessName()
        stackoverflow = website[0] + " " + website[1]
        removeChrome = website[-2] + " " + website[-1]
    except:
        print("Error handler:")
        RPC.update(details="Relaxing", large_image="relax", large_text=hoverText, small_image="dnd",
                   small_text="Do not disturb",
                   buttons=[{"label": "Join Discord", "url": "https://discord.gg/dxVxWZejYG"}])
    print(removeChrome)
    #Chrome support only for now

    if window_name == "chrome.exe":

        if website[-4] == "YouTube":

            print("you are on youtube")
            RPC.update(details=GetWindowText(GetForegroundWindow()),state="On YouTube", large_image="youtube", large_text=hoverText,
                       small_image="dnd")
        elif website[-4] == "Search":
            print("you are on stack google search")
            RPC.update(details=GetWindowText(GetForegroundWindow()), state="On stack overflow", large_image="googlesearch",
                       large_text=hoverText,
                       small_image="dnd")
        elif stackoverflow == "Stack Overflow":
            del website[-3:]
            final = " "



            RPC.update(details=final.join(website), state="On stack overflow",
                       large_image="stackoverflow",
                       large_text=hoverText,
                       small_image="dnd")
        elif removeChrome == "YouTube Music":

            del website[-3:]
            final = " "

            RPC.update(details=final.join(website), state="YouTube Music", large_image="youtubemusic",
                       large_text=hoverText,
                       small_image="dnd")


    elif window_name == "pycharm64.exe":

        #print("PyCharm is running")
        project_name = GetWindowText(GetForegroundWindow()).split()
        #print(project_name[0])
        RPC.update(details="Working on \n" + str(project_name[0]),state="Editing "+ str(project_name[2]), large_image="pycharm", large_text=hoverText, small_image="online", start=timestamp)
    else:
        RPC.update(details="Relaxing", large_image="relax", large_text=hoverText, small_image="dnd",
                  small_text="Do not disturb", buttons=[{"label": "Join Discord", "url": "https://discord.gg/dxVxWZejYG"}])


    time.sleep(5)
