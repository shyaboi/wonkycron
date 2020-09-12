import os
import time
import random
from datetime import date

timeStamp = date.today()

hour = time.strftime("%H")
minn = time.strftime("%M")
sec = time.strftime("%S")
nowTime = f"{hour}:{minn};{sec}"
f= open("muhfile.txt","a+")
print(nowTime)

def cronLoop():
    rando = random.randrange(244, 456)
    print(rando)
    f.write(f"\nLast cronned at: {timeStamp} | {nowTime}\n")
    os.system('node index.js /F');print("ran node cronish")
    time.sleep(rando)
    cronLoop()
cronLoop()
