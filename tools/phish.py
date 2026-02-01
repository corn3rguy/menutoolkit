import os
import sys
import time
import subprocess
def clear():
    os.system("clear")
clear()

def banner():
    print("""
██████╗░██╗░░██╗██╗░██████╗██╗░░██╗  ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
██╔══██╗██║░░██║██║██╔════╝██║░░██║  ████╗░████║██╔════╝████╗░██║██║░░░██║
██████╔╝███████║██║╚█████╗░███████║  ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██╔═══╝░██╔══██║██║░╚═══██╗██╔══██║  ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░░░░░██║░░██║██║██████╔╝██║░░██║  ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░""")

def phishmenu():
    print("""
╔═════════════════════════════════╗
║ 1. NexPhisher :D                ║
║ 2. ZPhisher (Famous) :D         ║
║ 3. MaskPhish (mask the url) :D  ║
║ 4. BlackEye :D                  ║
║ 5. HiddenEye_Legacy :D          ║
║ 6. GoPhish (also famous) :D     ║
║ 7. Evilginx2                    ║
║ 8. SocialPhish                  ║
║99. Exit :D                      ║
╚═════════════════════════════════╝""")
    
confirm = input("Install git? (y/n): ").strip().lower()
if confirm in ("y", "yes"):
    subprocess.run(("sudo", "apt", "install", "-y", "git"))
else:
    print("Script won't work without it :D")
time.sleep(2)
clear()

print("Welcome here twin :D")
time.sleep(1)
banner()

while True:
    phish_choice = input("phish>> ").strip().lower()

    if phish_choice in ("h", "help"):
        phishmenu()

    elif phish_choice in ("1", "nexphisher"):
        subprocess.run(("git", "clone", "https://github.com/htr-tech/nexphisher"))

    elif phish_choice in ("2", "zphisher"):
        subprocess.run(("git", "clone", "https://github.com/htr-tech/zphisher"))

    elif phish_choice in ("3", "maskphish"):
        subprocess.run(("git", "clone", "https://github.com/jaykali/maskphish"))

    elif phish_choice in (("4", "blackeye")):
        subprocess.run(("git", "clone", "https://github.com/shuvo-halder/blackeye"))

    elif phish_choice in ("5", "hiddeneye_legacy", "hiddeneyelegacy"):
        subprocess.run(("git", "clone", "https://github.com/Morsmalleo/HiddenEye_Legacy", "hiddeneyelegacy"))

    elif phish_choice in ("6", "gophish"):
        subprocess.run(("git", "clone", "https://github.com/gophish/gophish"))

    elif phish_choice in ("7", "evilginx2"):
        subprocess.run(("git", "clone", "https://github.com/kgretzky/evilginx2"))
    
    elif phish_choice in ("8", "socalphish"):
        subprocess.run(("git", "clone", "https://github.com/UndeadSec/SocialFish", "socialphish"))
    
    elif phish_choice in ("clear", "cls"):
        clear()

    elif phish_choice in ("99", "exit", "quit"):
        clear()
        print("Exiting... :D")
        time.sleep(0.5)
        sys.exit()
    