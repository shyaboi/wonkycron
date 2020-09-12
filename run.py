import os
import time

def cronLoop():
    os.system('node index.js /F');print("ran node cronish")
    time.sleep(.3)
    cronLoop()
cronLoop()
