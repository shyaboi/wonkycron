import os
import time
import datetime
from datetime import date
timeStamp = date.today()

hour = time.strftime("%H")
minn = time.strftime("%M")
sec = time.strftime("%S")
nowTime = "{hour}:{minn};{sec}"
f= open("muhfile.txt","a+")
print(nowTime)

def cronLoop():
    f.write("\nLast cronned at: {timeStamp} | {nowTime}\n")
    os.system('node index.js /F');print("ran node cronish")
    time.sleep(300)
    cronLoop()
cronLoop()
