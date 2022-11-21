# ECEN-404-Smart-Luggage 
Final Demo Video: https://youtu.be/8k7Zm0G9--M
## Shared repository for ECEN 404 Team 05 Smart Luggage  
SmartLuggage.zip contains Android Studio phone app code in java  
LatLng_code.zip contains the Python code for obtaining the latitude and longitude on the raspberry pi  
SabertoothDriver.py file include the motor driver linrary that controls the movement of the rover using raspberry pi.
ObstacleAvoid.py file include the obstacle avoidance algorithm using ultrasonic sensors.
integrate2.py file include the integration between the movement, tracking, and obstacle avoidance.


============================== Bi-weekly Update ================================

============================== Status Update 1  ================================

------------------------------ Movement and Obstacle Avoidance  - Assem Ahmed ----------------------

1. Integrating IMU unit with my subsystem to measure the distance and rotational angle of the rover.
2. Witing the code that recieves the (x, y) coordinates of the user from the tracking system.

Note: The IMU was found to be not a good fit later to measure the rotational angle of the rover due to inaccuracy.

------------------------------ Phone App - Angus Mckellar ------------------------------------------

1. Remodeled app for cleaner UI and efficiency.  
2. Weather app accurately displays weather for inputed city.  

------------------------------ Tracking and Navigation  - Tien Le ---------------------------------
1. Tracking the tag lcation. 
2. Calculating the distance from the tag to the initiator anchor.


============================== Status Update 2  ================================

------------------------------ Movement and Obstacle Avoidance  - Assem Ahmed ----------------------

1. Found out that IMU is not a good fit to measure the rotational angle of the rover due to inaccuracy.
2. Replaced the rover's batteries and tested the rover.

------------------------------ Phone App - Angus Mckellar ------------------------------------------

1. Create vector map of the users journey and display it for the user.  
2. Obtained raspberry pi and necessary code for gps module.  

------------------------------ Tracking and Navigation  - Tien Le ---------------------------------

1. Making improvement in tracking the tag location

============================== Status Update 3  ================================

------------------------------ Movement and Obstacle Avoidance  - Assem Ahmed ----------------------

1. Tested the obstacle avoidance from 403.
2. Recalibrated the movement system with the new batteries.
3. Soldered the ultrasonic sensors circuits on Perf Boards.
4. Started the integration between the movement system and the tracking system.

------------------------------ Phone App - Angus Mckellar ------------------------------------------

1. Set up raspberry pi with gps module.  
2. Finshed testing vector map of users journey.  

------------------------------ Tracking and Navigation  - Tien Le ---------------------------------
1. Slowing down the data rate from the the tag.
2. Improving the accuracy of the tag.


============================== Status Update 4  ================================

------------------------------ Movement and Obstacle Avoidance  - Assem Ahmed ----------------------
1. Integrated the movement subsystem with the tracking subsystem, but we’re facing problems.
2. The (x, y) coordinates received from the tracking subsystem has uncertainty. 
3. The data is not refreshed quickly enough, which makes the rover to over turn.
4. Started the integration of the obstacle avoidance subsystem.

------------------------------ Phone App - Angus Mckellar ------------------------------------------
1. Successfully get latitude and longitude of the raspberry pi.
2. Upload latitude and longitude to simple web server on local network.
3. Successfully access the local web server from Android app.

------------------------------ Tracking and Navigation  - Tien Le ---------------------------------
1. Finished setting the hardware with anchors, tag & gateway.
2. Collecting and calculating the distance between the tag to each anchors and tag position as x, y coordinate.
3. Verified the correct distance and cleaned the data.
4. Sending data to Movement subsystem.
5. Providing GPS data for the phone app.

============================== Status Update 5  ================================
Note: All subsystems were fully integrated before status update 5

------------------------------ Movement and Obstacle Avoidance  - Assem Ahmed ----------------------
1. Fully integrated the movement and obstacle avoidance with the tracking subsystem. 
2. Implemented a fail-safe solution to prevent the rover from going out of control.
3. Performed an overall validation for the system.
4. Continue to perform further validation and optimization to the system.
------------------------------ Phone App - Angus Mckellar ------------------------------------------
1. Successfully obtain latitude and longitude of raspberry pi on the phone.
2. Able to display the location of the luggage on the map along with the users location.
3. Continue to optimize and validate app to create the best user experience.
------------------------------ Tracking and Navigation  - Tien Le ---------------------------------
1. Finished setting the hardware with anchors, tag & gateway.
2. Collected and calculated the distance between the tag to each anchors and tag position as x, y coordinate.
3. Verified the correct distance and cleaned the data.
4. Provided GPS data for the phone app.
5. Sent data to Movement subsystem.

============================== Final Presentation  ================================
Note: System Validation was completed before the final presentation.

------------------------------ Movement and Obstacle Avoidance  - Assem Ahmed ----------------------
1. Configured motor driver with Raspberry Pi.
2. Created and tested python library for the motor driver for movement control.
3. Configured and tested ultrasonic sensors with Raspberry Pi to get the correct distances.
4. Created a top module that receives the (x, y) coordinates of the user and outputs the commands for the rover to follow the user.
5. Integrated obstacle avoidance with the top module.
6. Added a buzzer to alarm the user when the rover fails to follow him or is lost.
------------------------------ Phone App - Angus Mckellar ------------------------------------------

------------------------------ Tracking and Navigation  - Tien Le ---------------------------------

============================== Post Final Presentation  ================================

------------------------------ Team ----------------------------------------------------
1. System was validated indoor and outdoor while a weight load is added on the top.
2. All the system requirements are met.
3. Validation cases were validated and recorded: https://youtu.be/8k7Zm0G9--M



