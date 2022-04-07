
#Chase Ashby Covert Channel Import File
import socket
import array
import argparse
import struct
import sys

#Import Functio
def Sender(packet):
    receiver = '127.0.0.1'
    destinationPort = 1234

    #Param1 = IPv4 Setting
    #Param2 = Raw Socket indication
    #Param3 = IP Header

    sockets = socket.socket( socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW )
    print( "Socket Created:" )

    #Binding socket to getter
    sockets.bind( ( receiver, destinationPort ) )
    print("Socket Binded " + str(receiver) + "to destinationPort" + str(destinationPort))

    #Takes in bytes and an address and sends the data
    sockets.sendto(packet, (receiver, destinationPort))
    print("Packets sending to " + receiver + " at destinationPort " + str(destinationPort))
