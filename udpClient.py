#Russel Tagaca
#udpClient.py

import sys, time
import socket
import struct
from decimal import getcontext, Decimal

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

argv = sys.argv
host = argv[1]
port = int(argv[2])

bufSize = 10000
successPckt = 0
roundTrips = []
#port = int(port)
bufSize = int(bufSize)
getcontext().prec = 6


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Pinging " + host + ", " + str(port) + ":")
for i in range(1,11):
        x = [1, i]
        msgConvert = struct.pack('>ii', 1, i)
        print(msgConvert)
        #send data to server through sendto method
        timeNow = time.time()
        clientSocket.sendto(msgConvert, (host, port))
        time.sleep(2)       
        #receive data from server response
        clientSocket.settimeout(1.0)
        try:
            msgResponse,address = clientSocket.recvfrom(bufSize)
        except:
            print("Ping message number " + str(i) + " timed out")
            continue;
        timeDif = time.time() - timeNow
        roundTrips.append(round(timeDif, 6))
        #print received data from server
        print("Ping message number " + str(i) + " RTT: " + str(round(timeDif,6)) + " secs")
        successPckt += 1

print("Number of packets sent: 10, received: " + str(successPckt) + ", lost: " + "{0:.0f}%".format((10-successPckt)/10 * 100))
print("Min: " + str(min(roundTrips)) + ", Max: " + str(max(roundTrips)) + ", Average " + str(round(sum(roundTrips)/len(roundTrips),6)) + " RTT for all successful pings")
clientSocket.close()
