import sys
import argparse
import importer
import Getter
import struct
import socket
import array
import binascii

#Creating Raw Packet

def main(argv):
    args = parser()
    ArrayOfLines = createArrayOfLines()
    

    #Makes Decisions Based on Importer Arguments
    if args.action == True:

        for i in range( len( ArrayOfLines ) ):

            importer.Sender( createTCPPacket( args, ArrayOfLines[i] ) )
    else:
        importer.importer()

#Arguments to Be Parsed
def parser():
    parser = argparse.ArgumentParser(desc = 'Inputs Processing' )

    #Args for sending or receiving
    #Defaults as importer

    parser.add_argument('--importer', dest='action', action='store_true')
    parser.add_argument('--importer', dest='action', action='store_false')
    parser.set_defaults(action=True)

    args = parser.parse_args()

    return args


#Message Extraction
def retrieveMessage():
    messageFile = open(__file__ + "/../../data/message.txt")
    retrievedMessage = messageFile.read()
    messageFile.close()

    return retrievedMessage



#Transition to Binary
def binaryConversion():
    retrievedMessage = retrieveMessage()
    binaryCovertMessage = "{0:08b}".format(int(retrievedMessage, 16))
    return binaryCovertMessage


#converting to hex array for tcp packet
def createArrayOfLines():
    binaryString = binaryConversion()
    ArrayOfLines = []
    for i in range(len(binaryString)):
        if binaryString[i] == '0':
            ArrayOfLines.append(b'\x50\x00\x71\x10')
        else:
            ArrayOfLines.append(b'\x50\x02\x71\x10')

    return ArrayOfLines

#Creates TCP Packet
def createTCPPacket(args, newLine):
    header  = b'\x45\x00\x00\x28'  
    header += b'\xab\xcd\x00\x00'  
    header += b'\x40\x06\xa6\xec'  
    header += b'\x7f\x00\x00\x01'  
    header += b'\x7f\x00\x00\x01'  

    headert  = b'\x30\x39\x00\x50' 
    headert += b'\x00\x00\x00\x00' 
    headert += b'\x00\x00\x00\x00' 

    
    headert += newLine          
    headert += b'\xe6\x32\x00\x00'
    data = b'NewWorld'

    packet = headert + data

    return packet

main(sys.argv)