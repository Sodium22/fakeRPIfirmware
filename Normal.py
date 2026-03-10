"""
Normal.py is most of the code for the gui (Frontend.py) and will be used for all processing and stuff like that.


Normal.py opens Frontend.py using subprocess and sys. Frontend is the ui for normal, normal is used for the
operations and code while frontend is the ui using normals code.
its only separated so the ui doesn't break if things in normal have to be changed or updated so only one file has to
be fixed or changed

if subsystem and sys are used to open the second script like it's done here both scripts will be active at once
"""

"""
    To-Do
- add a "sleep" mode for main so it pulls less resources while normal or debug are on/used.
- 
"""
import time
import os
from pathlib import Path
import subprocess
import sys
from tqdm import tqdm
import random
import threading
import keyboard

print("getting ui ready")
time.sleep(.5)
print("You can go back to Main at any time by pressing esc")
time.sleep(.5)



IntroBar = random.randint(7, 17)
while IntroBar != 0:
    try:
        for i in tqdm(range(IntroBar)):
            IntroBar -= 1
            time.sleep(0.274)


    except:
        print("ERROR with tqdm loading bar")

procUI = subprocess.Popen([sys.executable, "Frontend.py"])

