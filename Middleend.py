import os
import time

while True:
    print("*" * 30)
    browse = int(input("Mode Select\n___________ \n Wifi(1) \n Bluetooth(2) \n Bad USB(3) \n Browse(4) \n> Selection: "))
    print("*" * 30)
    if browse == 1:  # Wifi
        print(">Wifi<")
        print(" Sniffer(1)")
        print(" Attacks(2)")
        print(" other(3)")

        wifimode = int(input("> Select: "))

        if wifimode == 1:  # Sniffer
            print("*" * 30)
            browseWIFISniff = int(
                input("Sniff Selection \n_______________  \n IPv6 Target Scan \n SSID scan \nAP Scan \n> Selection: "))

            if browseWIFISniff == 1:  # IPv6 Scan3

                IPTargetSIX = float(input("IP Target: "))
                time.sleep(0.5)
                os.system("clear")
                print("Confirm IP: ", IPTargetSIX)
                conf = input("Scan Target? \ny/n: ")
                if conf == "y":
                    os.system("nmap -6 " + IPTargetSIX)  # IPv6 Scan Command
                elif conf == "n":
                    print("Returning to Browse")
                    time.sleep(2)
                    continue

            elif browseWIFISniff == 2:  # SSIID scan

                # use kismet for ssid scan

                ex = input("Extra Info? (y/n)")

                if ex == "y":
                    os.system("")  # Kismet command for ssid scan and extra info aswell as hidden ssids

                elif ex == "n":
                    os.system("")  # Kismet command for simple ssid scan


            elif browseWIFISniff == 3:  # AP Scan

                # Kismet ap scan
                print("AP Scan:")
                os.system("")

        elif wifimode == 2:  # Attacks
            print("*" * 30)
            browseWIFIAttacks = int(input(
                "Attack Selection \n________________ \n Deauth Flood \n Deauth SSID Target \n Beacon Spam Flood \n> Selection: "))

            if browseWIFIAttacks == 1:  # Deauth Flood
                con = input("Confirm (y/n): ")
                os.system("")  # Add Deauth Command


        elif wifimode == 3:  # other
            print("*" * 30)






    #(4) Browse is used for searching things without an internet connection with things like wikipedia
    #add more browsing options like specific "books" for plants animals and whatever else
    elif browse == 4:
        print("Please select a browsing option: \n Wikipedia(1)")
        browseSelect = int(input("> Select: "))

        if browseSelect == 1:
            print("Wikipedia Selected...")
            time.sleep(1.5)
            #open a .zim wikipedia file with kiwix tools and add a search option before opening
            #it to directly open it to the right page