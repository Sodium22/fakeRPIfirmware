import random
import datetime
import secrets
import sys
import time
import os
import subprocess

#V: P0.1 made on the 09.01.26 (from around 9:30 to 12:30 CET)(at rbb greifswald)

#add password with encryption, code to switch between terminal (raspi OS) and custom fakeware (fake firmware)
#Terminal commands mostly still missing, middle Script + link between both missing
#change the selection from typing numbers to selecting with arrow keys and enter (for the back and middle end)
#Add command outputs for library specific clt commands (SSIDs, deauth packages etc. )
#add the full file path under Terminal and middleend

#add ssh ceck for raspi-config if off os.system("sudo raspi-config")

#Kismet , Aircrack-ng suite , bettercap

while True:
    Version = "V: P0.1"

    print("*" * 30)


    sAnim = random.randint(1, 3)

    if sAnim == 1:
        print(r"/\____/\ " + "\n| * - *| \n >" , Version)

    elif sAnim == 2:
        print(r"/\____/\ " + "\n| o   o| \n >" , Version)


    elif sAnim == 3:
        print(r"/\____/\ " + "\n| § _ §| \n >" , Version)

    print("\n", datetime.datetime.now(datetime.timezone.utc).astimezone().strftime("%d %B %A"))
    print("*" * 30)
    time.sleep(0.5)



    modeID = int(input("Debug\nTools\nPentest\nOS Terminal"))

    if modeID == 1:
        print("*" * 30)
        print("Debug")
        debugSelect = int(input("Debug over ssh\nDebug over OS terminal"))

        if debugSelect == 1:
            print("Debug over ssh")
            ip = os.system("")              #Add get ip command
            username = os.system("")        #Add get user command

            print(ip)
            print("Connect to ", username, "@", ip, "over ssh on another machine")
        elif modeID == 2:
            print("Debug over Terminal")
            time.sleep(3)
            try:
                programmID = os.system("sudo ps aux | grep -i name_of_program")
            except os.error as e:
                print(f"Error while looking for program ID: \n{e}")
            print("Launching OS terminal...")
            time.sleep(1.5)
            os.system(f"sudo kill -9 {programmID}")

