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
╔════════════════════════════════╗
║                                ║
║   Coming soon don't worry :D   ║
║                                ║
║ 99. Exit :D                    ║
╚════════════════════════════════╝ 
          """)

clear()
dos_banner()

while True:
    dos_choice = input("dos (coming soon)>> ")
    if dos_choice in ("h", "help"):
        dos_menu()
    elif dos_choice in ("99", "exit", "quit"):
        clear()
        print("Exitting :D")
        time.sleep(0.5)
        sys.exit()
    else:
        print("Command not available at this moment :D")