from re import X
import serial
import time
import datetime
from math import *

def navigation():
    DWM=serial.Serial(port="/dev/ttyACM0", baudrate=115200)
    print("Connected to " +DWM.name)
    DWM.write("\r\r".encode())
    time.sleep(1)
    DWM.write("lec\r".encode())
    time.sleep(1)

    count = 0
    while True:
        try:
            line=DWM.readline()
            print(type(line))
            if(line):
                print("Line1 is",line)
                parse=line.decode().split(",")
                print(parse)
                if parse[0]=="POS":
                    pos_AN0=(parse[parse.index("D3A8")+1],parse[parse.index("D3A8")+2],parse[parse.index("D3A8")+3])
                
                    print(datetime.datetime.now().strftime("%H:%M:%S"),pos_AN0)
                
                    #Filter X coordinate
                    x_pos=parse[parse.index("POS")+3]
                    #print ("Xpos",x_pos, " Type ",type(x_pos))
                    new_x =float(x_pos)
                    print ("x coordinate: ",new_x, " Type ",type(new_x))
                
                    #Filter Y coordinate
                    y_pos=parse[parse.index("POS")+4]
                    #print ("Ypos",y_pos, " Type ",type(y_pos))
                    new_y =float(y_pos)
                    print ("y coordinate: ",new_y, " Type ",type(new_y))
                
                    Distance = sqrt(new_x**2 + new_y**2)
                    print("Distance is ",Distance)
                    print()
                
                    #Skip if result is nan, otherwise will take value in 3 second
                    if (x_pos !="nan"):
                        time.sleep(3)
                    else:
                        time.sleep(0.1)
                    count = count +1
                    print("count time:" ,count)

                
                else:
                    print("Distance not calculated: ",line.decode())
        except Exception as ex:
            print(ex)
            break
    #DWM.write("\r".encode())
    #DWM.close()
    return x_pos,y_pos

x = 0
y = 0
for  i in range(0,120):
    x,y -= navigation()