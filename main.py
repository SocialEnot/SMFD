import os, re
import platform
import threading
import socket
from datetime import datetime
import colorama
from colorama import *
colorama.init()
import socket

hostt = socket.gethostbyname(socket.getfqdn())

def main():
    port = 5552
    s = socket.socket()
    s.bind((hostt,port))
 
    s.listen(1)
    print(Fore.RED + "Listening port 5552")
    connection, address = s.accept()
    print(Fore.WHITE + "Connection  " + str(address))
    while True:
        try:
            print(Fore.RED)
            toSend = input("[connect]>SMFD> ")
            connection.send(toSend.encode())
            data = connection.recv(1024).decode()
            print(data)
        except:
            break
    print("Connection refused")
    connection.close()
 

banner = """
░██████╗███╗░░░███╗███████╗██████╗░
██╔════╝████╗░████║██╔════╝██╔══██╗
╚█████╗░██╔████╔██║█████╗░░██║░░██║
░╚═══██╗██║╚██╔╝██║██╔══╝░░██║░░██║
██████╔╝██║░╚═╝░██║██║░░░░░██████╔╝
╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═════╝░"""

print(Fore.RED + banner)

veav = input(">SMFD> ")
if veav == 'total_scan_devices':
    print(hostt)
    if __name__ == '__main__':
        main()
