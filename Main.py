import time as t
import datetime
import random
import keyboard
from tqdm import tqdm
from tqdm import trange
from colorama import Fore
from pathlib import Path
import subprocess
import sys
import threading

"""
    hardware notes
> the main build is gonna be big (size of a laptop probably) 
   with a remote kind of thing with a display and tiny keyboard wich will use the "laptops" hard and software
   

"""
"""
        To-Do
        -----
    - Button Control With keyboard keys                                                     < x >
    - fix progress bar to only display once and then run the rest of the program            < x >
    - help/explanation of modes (short not in detail thats for git)                         < x >    
    - add normal and debug modes as 2 seperate scripts that can swap around with this one   < x >
    - add offline and updating wiki support with kiwix tools                                <  > 
    - full ui for normal mode (tk or something similar)                                     <  >
    - tk list with all scripts and a way to execute them from tk                            < x >
    - save output button for TK and code output in TK not the console                       <  >
    - add hibernation logic to Main, Debug and normal                                       <  >
    - add a "go back" option to Normal and Debug to return to main at any time              < x > (?) (not tested yet, but implemented)
    - test scripts that need specific libraries or nmap for example (with TKs list)         < x > (seem to work but nmap and similar not tested yet, just basic libraries)
    - implement the actual debug mode with useful stuff                                     <  >
    - switch the TK ui for customTK or another ui librarie in a newer version               <  >
    - replace the TK ui with a PyQt6 ui                                                     <  >
    
"""


while True:

    def userleavecheck():
        while True:
            if keyboard.is_pressed("esc"):
                procNormal.terminate()
                #procDebug.terminate()
                t.sleep(.2)

    T = threading.Thread(target = userleavecheck)
    T.daemon = True
    T.start()



    IntroBar = random.randint(5, 17)
    while IntroBar != 0:
        try:
            for i in tqdm(range(IntroBar)):
                IntroBar -= 1
                t.sleep(0.274)

        except:
            break


    while True:
        Version = "V: P0.2"
        print("*" * 30)


        sAnim = random.randint(1, 3)


        if sAnim == 1:
            print(r"/\____/\ " + "\n| * - *| \n >" , Version)

        elif sAnim == 2:
            print(r"/\____/\ " + "\n| o   o| \n >" , Version)


        elif sAnim == 3:
            print(r"/\____/\ " + "\n| § _ §| \n >" , Version)



        print("\n", datetime.datetime.now(datetime.timezone.utc).astimezone().strftime("%d %B %A"))
        print("yes this is the right version the UI is only in the normal mode")
        print("*" * 30)
        t.sleep(0.5)
        timer = 5
        DebugReqeust = "1"
        print("< Press Enter For Debug mode or Backspace For normal mode >")
        print("        # Or press H for more info on both modes #"        )
        while True:
            try:
                if keyboard.is_pressed("H"):
                    print("-" * 20)
                    print("The Debug Mode is for fixing small issues and troubleshooting. \nReal fixes need to be made on a different device with the source files")
                    print("The Normal Mode is the usual ui youll interact with. It has all tools libraries and commands unlike the debug mode wich only has specific debugging commands")
                    print("\nYou will be sent back to mode select in 10 seconds.")

                    HelpExit = 10
                    while HelpExit > 0:
                        for i in tqdm(range(HelpExit)):
                            HelpExit -= 1
                            t.sleep(1)
                    break




                elif keyboard.is_pressed("Backspace"):
                    print("-" * 20)
                    print("normal mode selected \n-- Please Wait --")
                    t.sleep(1.5)
                    procNormal =  subprocess.Popen([sys.executable, "Normal.py"])  #add hibernation logic


                    break

                elif timer == 0:
                    print("*§ Timeout Error §*")
                    t.sleep(1.5)
                    break

                """elif keyboard.is_pressed("Enter"):
                                   print("-" * 20)
                                   print("Debug Mode Selected \n__ Please Wait __")
                                   t.sleep(2)
                                   procDebug = subprocess.Popen([sys.executable, "Debug.py"])   #add hibernation logic

                                   break

                    elif timer == 0:
                        print("*# Timeout Error #*")
                        t.sleep(1.5)
                        break"""

            except:
                break




























