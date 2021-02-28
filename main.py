
import psutil
from pypresence import Presence
import time
import os
from win32gui import GetWindowText, GetForegroundWindow

from utils.WindowUtil import getActiveProcessName
from dotenv import load_dotenv
load_dotenv()


client_id = os.environ.get("clientid")
hoverText = os.environ.get("hoverText")

RPC = Presence(client_id,pipe=0)
RPC.connect()
print(getActiveProcessName())




while True:  # The presence will stay on as long as the program is running

    window_name = getActiveProcessName()
    if window_name == "chrome.exe":
        print(window_name)
        RPC.update(details=GetWindowText(GetForegroundWindow()), large_image="chrome", large_text=hoverText, small_image="dnd")
    elif window_name == "pycharm64.exe":
        print(window_name)
        print("PyCharm is running")
        RPC.update(details="Working on " + GetWindowText(GetForegroundWindow()), large_image="pycharm", large_text=hoverText, small_image="online")
    else:
        continue
        #RPC.update(details="Relaxing", large_image="relax", large_text=hoverText, small_image="dnd",
        #          small_text="Do not disturb", buttons=[{"label": "Join server", "url": "https://discord.gg/dxVxWZejYG"}])


    time.sleep(2) # Can only update rich presence every 15 seconds
