import win32process
from win32gui import GetForegroundWindow
import psutil
def getActiveProcessName():
    try:
        pid = win32process.GetWindowThreadProcessId(GetForegroundWindow())
        return(psutil.Process(pid[-1]).name())
    except:
        pass