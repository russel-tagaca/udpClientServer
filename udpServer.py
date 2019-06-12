#Russel Tagaca
#udpServer.py

import sys
import time
import socket
import struct
import random

serverIp = "127.0.0.1"
serverPort = 12000
dataLen = 10000000
responseCount = 0;
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#takes IPaddress and port # to socket
serverSocket.bind((serverIp, serverPort))

print('The server is ready to receive on port: ' + str(serverPort))

#loop forever to listen to datagram messages
while True:
    
    #receive and print client data from "data" socket
    data, address = serverSocket.recvfrom(dataLen)
    if (data):
        dataUnpack = struct.unpack('>ii', data)
        responseCount += 1
        if (random.randint(1,11) < 4):
            print("Message with sequence number " + str(dataUnpack[1]) + " dropped")
            continue;
    #send back to client
        else:
            print("Responding to ping request with sequence number " + str(dataUnpack[1]))
            msgResponse = struct.pack('>ii', 1, dataUnpack[1])
            serverSocket.sendto(msgResponse,address)
