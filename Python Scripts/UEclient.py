import zmq
import uuid

c = zmq.Context()
s = c.socket(zmq.PAIR)
s.bind('tcp://*:1254')

def FetchOrd():
    Xinp = None
    Yinp = None
    while Xinp == None:
        Xinp = int(input("Enter x co-ordinate:"))
        
    while Yinp == None:
        Yinp = int(input("Enter y co-ordinate:"))
    
    
    return Xinp,Yinp


rec = "0"
while True:
    
    id = uuid.uuid4()
    
    print('PACKAGE CO-ORDINATES:')
    pkg = FetchOrd()
    print('DEST CO-ORDINATES:')
    dest = FetchOrd()
    s.send_string(f"{str(id)},{str(pkg)},{str(dest)}")
    
     
    
