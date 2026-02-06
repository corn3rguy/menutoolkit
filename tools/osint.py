import sys
import os
import webbrowser
import time 
import subprocess
def clear():
    os.system("clear")

def banner():
    print("""
   ___    ____    ___   _   _   _____     _____    ___     ___    _     
  / _ \  / ___|  |_ _| | \ | | |_   _|   |_   _|  / _ \   / _ \  | |    
 | | | | \___ \   | |  |  \| |   | |       | |   | | | | | | | | | |    
 | |_| |  ___) |  | |  | |\  |   | |       | |   | |_| | | |_| | | |___ 
  \___/  |____/  |___| |_| \_|   |_|       |_|    \___/   \___/  |_____|
""")

def helpmenu():
    print("""Menu Options:
1. OSINT Framework (website)
2. PhoneInfoGa
3. Sherlock
4. Instant Username Search
5. ThatsThem
6. Exit""")

clear()
banner()
while True:
    osintch = input(">> ").strip().lower()

    if osintch in ("help", "h"):
        helpmenu()
    elif osintch in ("1", "osintfrm",):
        print("OSINT FrameWork opened.")
        webbrowser.open("https://osintframework.com")
    elif osintch in ("2", "phoneinfoga"):
        installchk = input("Do you have pip installed? y/n: ").strip().lower()
        if installchk == "y":
            subprocess.run(("pip", "install", "phoneinfoga"))
        elif installchk == "n":
            print("Then go install it.")
    
    elif osintch in ("3", "sherlock"):
        shchoice = input("select git or pip>> ").strip().lower()
        if shchoice == "git":
            subprocess.run(("git", "clone", "https://github.com/sherlock-project/sherlock"))
        elif shchoice == "pip":
            subprocess.run(("pip", "install", "sherlock"))

    elif osintch in ("4", "ius"):
        print("Opening IUS in browser.")
        time.sleep(0.2)
        webbrowser.open("https://instantusername.com")

    elif osintch in ("5", "thatsthem"):
        print("Opening thatsthem in browser")
        time.sleep(0.2)
        webbrowser.open("https://thatsthem.com")
    
    elif osintch in ("clear", "cls"):
        clear()
    
    elif osintch in ("6", "exit"):
        print("Exiting...")
        time.sleep(0.4)
        sys.exit()

    else:
        print("What?")