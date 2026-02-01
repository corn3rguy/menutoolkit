import sys
import os
import time
import subprocess
def clear():
    os.system("clear")

print("Welcome :D")

user = input("What should we call you?: ")

print("okay", user, ":D")  
time.sleep(1)
clear()

def tool_banner():
    print("""
████████╗░█████╗░░█████╗░██╗░░░░░░██████╗  ██╗██████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝  ╚═╝██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░  ░░░██║░░██║
░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗  ░░░██║░░██║
░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝  ██╗██████╔╝
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░  ╚═╝╚═════╝░
""")

def help_menu():
    print("""
          Help menu :D
╔══════════════════════════════════╗
║ 1. Scanning tools :D             ║
║ 2. DoS (Denial of Service ) :D   ║
║ 3. Phising tools :D              ║
║ 99. Exit :D                      ║
║                                  ║
║     More comming soon... :D      ║
║                                  ║
║                                  ║
╚══════════════════════════════════╝        
""")

tool_banner()
while True:
    choice = input("Enter your choice " + user + ": ").strip().lower()

    if choice in ("h", "help"):
        help_menu()
    elif choice in ("1", "scanning tools", "scanning", "scan"):
        subprocess.run(("python", "tools/nw_scan.py"))
    elif choice in ("2", "dos"):
        subprocess.run(("python", "tools/dos.py"))
    elif choice in ("3", "phish", "phishing tools"):
        subprocess.run(("python", "tools/phish.py"))
    elif choice in ("99", "quit", "exit"):
        clear()
        print(user, "is exiting :D")
        time.sleep(0.5)
        sys.exit()
    elif choice in ("cls", "clear", "clr"):
        clear()
    elif choice in ("banner"):
        clear()
        tool_banner()
    else:
        print("""What are you typing xd :D
""")