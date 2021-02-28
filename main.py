from pypresence import Presence
import os
from win32gui import GetWindowText, GetForegroundWindow
import time
from utils.WindowUtil import getActiveProcessName
import threading
from dotenv import load_dotenv
load_dotenv()


client_id = os.environ.get("clientid")
hoverText = os.environ.get("hoverText")

RPC = Presence(client_id,pipe=0)
RPC.connect()

timestamp = time.time()



while True:  # The presence will stay on as long as the program is running

    window_name = getActiveProcessName()
    if window_name == "chrome.exe":

        RPC.update(details=GetWindowText(GetForegroundWindow()), large_image="chrome", large_text=hoverText, small_image="dnd")
    elif window_name == "pycharm64.exe":

        #print("PyCharm is running")
        project_name = GetWindowText(GetForegroundWindow()).split()
        #print(project_name[0])
        RPC.update(details="Working on \n" + str(project_name[0]),state="Editing "+ str(project_name[2]), large_image="pycharm", large_text=hoverText, small_image="online", start=timestamp)
    elif window_name:
        RPC.update(details="Relaxing", large_image="relax", large_text=hoverText, small_image="dnd",
                  small_text="Do not disturb", buttons=[{"label": "My Website", "url": "https://qtqt.cf"}])


    time.sleep(2) # Can only update rich presence every 2 seconds
