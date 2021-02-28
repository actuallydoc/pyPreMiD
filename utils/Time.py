import time
import threading


def startTimer():
    print(time.time())
    threading.Timer(1, startTimer).start()
if __name__ == '__main__':
    startTimer()
