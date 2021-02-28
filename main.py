import psutil
from pypresence import Presence
import time
import os
from utils.processHandler import checkIfProcessRunning
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get("clientid")
hoverText = os.environ.get("hoverText")

RPC = Presence(client_id,pipe=0)
RPC.connect()


while True:  # The presence will stay on as long as the program is running

    if checkIfProcessRunning("chrome.exe"):
        print("Chrome is running")
        RPC.update(details="Chrome", large_image="chrome", large_text=hoverText, small_image="dnd")
    elif checkIfProcessRunning("Discord.exe"):
        print("Discord is running")
        RPC.update(details="Discord", large_image="discord", large_text=hoverText, small_image="online")
    elif checkIfProcessRunning("flux.exe"):
        print("Discord is running")
        RPC.update(details="Flux", large_text=hoverText)
    else:
        RPC.update(details="Relaxing", large_image="relax")

    time.sleep(5) # Can only update rich presence every 15 seconds
