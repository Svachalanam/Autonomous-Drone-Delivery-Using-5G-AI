
import UdpComms as U
import time
import socket
import zmq
# Create UDP socket to use for sending (and receiving)
sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True)
c = zmq.Context()
s = c.socket(zmq.PAIR)
s.connect('tcp://127.0.0.1:1254')


def FetchOrd():
    Xinp = 200
    Yinp = 200
    while Xinp <=150 or Xinp >=100:
        Xinp = int(input("Enter x co-ordinate:"))
    while Yinp <=150 or Yinp >=100:
        Yinp = int(input("Enter y co-ordinate:"))
    
    
    return Xinp,Yinp




ids = []
packages = []
destinations = []

while True:
    
   
    text = str(s.recv())[1:]
    parts = text.split(',')

    if parts[0].strip() not in ids:
        ids.append(parts[0].strip())
        packages.append(parts[1].strip())  
        destinations.append(parts[2].strip())

    
    print(f"Recived order IDs, Pickup, Desitnation as:  {text}")

    data = " "
    sock.SendData(text)
    data = sock.ReadReceivedData()
    if data != None: 
        print(data) 

    
