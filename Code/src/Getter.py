#Chase Ashby Retrieval File Covert Channel
import socket
import struct
import collections
import os
import binascii

#Takes in array of received packets and pulls out the covert data
def retrieveMessage(datas):
    holder = []

    binMessage = []
    for i in range(len(datas)):

        if datas[i][33] == 2:
            binMessage.append('1')

        else:
            binMessage.append('0')

    binMessage = ''.join(binMessage)
    print("Binary Message: " + binMessage)
    binMessage = int(binMessage,2)
    print("Original Message" + hex(binMessage))

#Retrieval Function
def retrieve():

    #Destination Address
    environment = '127.0.0.1'
    destination = 1234

    #Making Raw Socket
    sockets = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    print("Socket Generated.")

    #Commbining environment with destination
    sockets.connect((environment, destination))
    print("Connected " + str(environment) + " on destination " + str(destination))

    #Check for packet reception
    datas = []

    while True:

        #Receives data 
        print("Checking for data")
        timeout = sockets.settimeout(5.0)
        try:
            data = sockets.recvfrom(1024)

        except socket.timeout:
                print("Data Transmission Complete")
                retrieveMessage(datas)
                break

        datas.append(data[0])

        #Printing information retrieved
        print("Byte Length " + str(len(data[0])))
        print("Printing Bits:")

        num = 0
        for ele in data[0]:

            if num == 20:
                print("THeader Information:")

            if num == 0:
                print("Kernel: ")

            if num == 40:
                print("Information: ")

            print((ele))
            num += 1

        print("Length of received data:" + str(len(data[1])))
        print("From socket: " + data[1][0])

    print("Retrieve Closed")