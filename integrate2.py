# This file only includes the integration between the Movement and tracking system
# with the obstacle avoidance

#from SabertoothDriverSimple import SerialMotorControl
from SabertoothDriverSimple import SerialMotorControl
#import the GPIO library
import RPi.GPIO as GPIO

import serial
import time
import datetime
from math import *

#define the USB port for the Raspberry Pi
motors = SerialMotorControl('/dev/ttyUSB0')
GPIO.setmode(GPIO.BOARD) ##
GPIO.setwarnings(False) ##

f = 25 #forward speed  #outdoor run at f = 25
t = 40 #turning speed  #outdoor run at f = 65

##================ Buzzer Function======================##

BUZZER_PIN = 7  # Buzzer pin number
GPIO.setup(BUZZER_PIN, GPIO.OUT)
def buzzer(duration, frequency):  # Play different frequencies
    print("buzzer")
    for i in range(duration):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(frequency)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(frequency)


##================ End of Buzzer Function==================##


##========== Obstacle Avoidance Function ========================##
# Define GPIO for ultrasonic central
GPIO_TRIGGER_CENTRAL = 16
GPIO_ECHO_CENTRAL = 18
GPIO.setup(GPIO_TRIGGER_CENTRAL, GPIO.OUT)  # Trigger > Out
GPIO.setup(GPIO_ECHO_CENTRAL, GPIO.IN)      # Echo < In

# Define GPIO for ultrasonic Right
GPIO_TRIGGER_RIGHT = 33
GPIO_ECHO_RIGHT = 35
GPIO.setup(GPIO_TRIGGER_RIGHT, GPIO.OUT)  # Trigger > Out
GPIO.setup(GPIO_ECHO_RIGHT, GPIO.IN)      # Echo < In

# Define GPIO for ultrasonic Left
GPIO_TRIGGER_LEFT = 38
GPIO_ECHO_LEFT = 40
GPIO.setup(GPIO_TRIGGER_LEFT, GPIO.OUT)  # Trigger > Out
GPIO.setup(GPIO_ECHO_LEFT, GPIO.IN)      # Echo < In

# Detect front obstacle
def frontobstacle():

    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER_CENTRAL, False)
    # Allow module to settle
    time.sleep(0.2)
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_CENTRAL, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_CENTRAL, False)
    # start measuring the time ECHO is HIGH
    start = time.time()
    while GPIO.input(GPIO_ECHO_CENTRAL) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO_CENTRAL) == 1:
        # record when ECHO is LOW
        stop = time.time()
    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # Multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000 / 2  # distance of both directions so divide by 2
    print("Front Distance : %.1f" % distance)
    return distance

def rightobstacle():
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER_RIGHT, False)
    # Allow module to settle
    time.sleep(0.2)
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_RIGHT, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_RIGHT, False)
    # start measuring the time ECHO is HIGH
    start = time.time()
    while GPIO.input(GPIO_ECHO_RIGHT) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO_RIGHT) == 1:
        stop = time.time()
        # record when ECHO is LOW
    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # Multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000 / 2  # Distance of both directions so divide by 2
    print("Right Distance : %.1f" % distance)
    return distance

def leftobstacle():
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER_LEFT, False)
    # Allow module to settle
    time.sleep(0.2)
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_LEFT, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_LEFT, False)
    # start measuring the time ECHO is HIGH
    start = time.time()
    while GPIO.input(GPIO_ECHO_LEFT) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO_LEFT) == 1:
        # record when ECHO is LOW
        stop = time.time()
    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # Multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000 / 2  # Distance of both directions so divide by 2
    print("Left Distance : %.1f" % distance)
    return distance

##========== Navigation Function ========================##
# This functions returns the (x,y) coordinates of the used relative
# to the rover - (0,0) coordinate

def start():
    DWM=serial.Serial(port="/dev/ttyACM0", baudrate=115200)
    print("Connected to 1st " +DWM.name)
    DWM.write("\r\r".encode())
    time.sleep(1)
frontDistance = frontobstacle()
def navigation():
    # open the serial connection with RPI
    DWM=serial.Serial(port="/dev/ttyACM0", baudrate=115200)
    print("Connected to " +DWM.name)
    
    time.sleep(0.04)
    DWM.write("l".encode())
    time.sleep(0.03)
    DWM.write("e".encode())
    time.sleep(0.03)
    DWM.write("c\r".encode())
    time.sleep(0.09)
    count = 0
    while True:
        try:
            line=DWM.readline()
            if(line):
                parse=line.decode().split(",")
              
                if parse[0]=="POS":
                    # get the x-coordinate position
                    x_pos=parse[parse.index("POS")+3]
                    new_x =float(x_pos)
                    # get the y-coordinate position
                    y_pos=parse[parse.index("POS")+4]
                    new_y =float(y_pos)
                    # check if non-valid value recieved
                    # if so, skip and recheck for a valid value
                    if (x_pos !="nan"):
                        break
                else:
                    print("Distance not calculated: ",line.decode())
        except Exception as ex:
            print(ex)
            break
    DWM.write("\r".encode())
    DWM.close()
    # return the new x,y coordinates
    return new_x,new_y
## ^^^^ END of Navigation Function ^^^^ ##

## Navigation and Movement integration ##
def integrate1():
    start = time.time()
    # Drive 5 minutes - just for testing
    # instead of while True:
    while start > time.time() - 600: # 300 = 60 seconds * 5
        # get the x, y coordinates of the rover
        x,y = navigation()
        print("Position is ",x, ",", y)
        changed = False
        # calculate the distance between the rover and the user
        Distance = sqrt(x**2 + y**2)
        print("Distance is: ",Distance)
        # while distance is greater than 3m, the rover is considered out of range
        # if the rover is out of range, stop the rover and trigger the buzzer
        while (Distance > 3):
            motors.stop() # stop
            # trigger the buzzer
            for i in range(30):
                buzzer(1, 5)
                break
            break
            # get the x, y coordinates of the rover
            x,y = navigation()
            print("Position is ",x, ",", y)
            # calculate the distance between the rover and the user
            Distance = sqrt(x**2 + y**2)
            print("Distance is: ",Distance)
            x_new, y_new = navigation()
            if ((abs(x_new - x)) > 0.2):
                # calculate the distance between the rover and the user
                Distance = sqrt(x**2 + y**2)
                print("Distance is: ",Distance)
                break
            elif ((abs(y_new - y)) > 0.2):
                # calculate the distance between the rover and the user
                Distance = sqrt(x**2 + y**2)
                print("Distance is: ",Distance)
                break
            # get the x, y coordinates of the rover
            x,y = navigation()
            print("Position is ",x, ",", y)
            # calculate the distance between the rover and the user
            Distance = sqrt(x**2 + y**2)
            print("Distance is: ",Distance)
        
        # while the x-axis is NOT between -0.4 m and 0.4 m
        while (x <= -0.4 or x >= 0.4):
            # if x > 0, turn left 
            if (x > 0):
                ## Check the obstacle on the left side before turning left
                # if there is an obstacle move forward until the obstacle is disappeared
                while leftobstacle() < 50:
                    print("1")
                    motors.stop()
                    time.sleep(0.2)
                    while (frontobstacle() < 50): ##before moving forward, check the front obstacle
                        motors.stop()         # stop completely if there is an obstacle
                    motors.drive_forward(f)
                    time.sleep(0.3) ## might need to be removed
                motors.drive_left(t)
            # if x < 0, turn right    
            if (x < 0):
                ## Check the obstacle on the right side before turning right
                # if there is an obstacle move forward until the obstacle is disappeared
                while rightobstacle() < 50:
                    
                    motors.stop()
                    time.sleep(0.2)
                    while (frontobstacle() < 60): ##before moving forward, check the front obstacle
                        motors.stop()          # stop completely if there is an obstacle
                    motors.drive_forward(f)
                    time.sleep(0.3) ## might need to be removed
                motors.drive_right(t)
                
            x,y = navigation()
            print("Position is ",x, ",", y)
        # get the x, y coordinates of the rover    
        motors.stop()
        time.sleep(0.3)
        
        ## Move forward until the distance between the rover and the user is 0.8 m
        while (Distance > 0.8 and frontobstacle() > 60):
            # get the x, y coordinates of the rover
            x,y = navigation()
            print("Position is ",x, ",", y)
            # calculate the distance between the rover and the user
            Distance = sqrt(x**2 + y**2)
            print("Distance is: ",Distance)
            x_new, y_new = navigation()
            if ((abs(x_new - x)) > 0.2):
                # calculate the distance between the rover and the user
                Distance = sqrt(x**2 + y**2)
                print("Distance is: ",Distance)
                break
            elif ((abs(y_new - y)) > 0.2):
                # calculate the distance between the rover and the user
                Distance = sqrt(x**2 + y**2)
                print("Distance is: ",Distance)
                break
            x,y = navigation()
            print("Position is ",x, ",", y)
            # calculate the distance between the rover and the user
            Distance = sqrt(x**2 + y**2)
            print("Distance is: ",Distance)
            x_new, y_new = navigation()
                ## when moving forward check for fron
            while frontobstacle() < 60:
                    motors.stop()
                    time.sleep(2)
                    # before turning left check for left obstacles
                    # if there is an obstacle stop and trigger the alarm
                    if (x > 0):
                        while leftobstacle() < 50:
                            motors.stop()
                            for i in range(30):
                                buzzer(1, 5)
                                break
                        motors.stop()
                        time.sleep(0.5)
                        motors.drive_left(t)
                        time.sleep(1.3)
                        motors.drive_forward(f)
                        time.sleep(0.2)
                    
                    if (x < 0):
                        # before turning right check for right obstacles
                        # if there is an obstacle stop and trigger the alarm
                        while rightobstacle() < 50:
                            motors.stop()
                            for i in range(30):
                                buzzer(1, 5)
                                break
                        motors.stop()
                        time.sleep(0.5)
                        motors.drive_right(t)
                        time.sleep(1.3)
                        motors.drive_forward(f)
                        time.sleep(0.2)
            #stop if front obstacle is < 50cm
            while frontobstacle() < 50:
                motors.stop    
            
            motors.drive_forward(f)
            # get the x, y coordinates of the rover
            x,y = navigation()
            print("Position is ",x, ",", y)
            # calculate the distance between the rover and the user
            Distance = sqrt(x**2 + y**2)
            print("Distance is: ",Distance)
        
        ## Stop when the distance between the rover and the user is less than 0.8m
        while (Distance <= 0.8):
            # get the x, y coordinates of the rover
            x,y = navigation()
            print("Position is ",x, ",", y)
            # calculate the distance between the rover and the user
            Distance = sqrt(x**2 + y**2)
            print("Distance is: ",Distance)
            x_new, y_new = navigation()
            if ((abs(x_new - x)) > 0.2):
                # calculate the distance between the rover and the user
                Distance = sqrt(x**2 + y**2)
                print("Distance is: ",Distance)
                break
            elif ((abs(y_new - y)) > 0.2):
                # calculate the distance between the rover and the user
                Distance = sqrt(x**2 + y**2)
                print("Distance is: ",Distance)
                break
            motors.stop() ## stop
            # get the x, y coordinates of the rover
            x,y = navigation()
            print("Position is ",x, ",", y)
            # calculate the distance between the rover and the user
            Distance = sqrt(x**2 + y**2)
            print("Distance is: ",Distance)

#  clear GPIOs function
def cleargpios():
    print("clearing GPIO")
    GPIO.output(16, False)
    GPIO.output(33, False)
    GPIO.output(38, False)
#    GPIO.output(7, False)
    print("All GPIOs CLEARED")
 
# The main function to run the program        
def main():
    cleargpios()
    start()
    integrate1()
# run the main function
if __name__ == "__main__":
    main()

