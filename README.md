# IoT Project - Bilbao-SportAir
This repository contains the source code and documentation for the final project of the IoT course.

## Repository Contents
- 'temhumTBCopia.py:' Script for reading and handling temperature and humidity data.

- 'airqualityTBCopia.py:' Script for handling air quality data.

- 'main.py:' Main file coordinating the functions of the above scripts.


## Usage Instructions
Clone this repository on your Raspberry Pi:


### Copy code
git clone https://github.com/jonmaestre/Bilbao-SportAir.git
cd Bilbao-SportAir
## Open and modify the scripts as needed using the nano editor:


### Copy code
- nano temhumTBCopia.py
- nano airqualityTBCopia.py
- nano main.py
### Make the necessary modifications and save the changes.

## Run the main script:


### Copy code
- 'sudo python3 temhumTBCopia.py': To execute the temperatura  file and show the datas 
- 'sudo python3 airqualityTBCopia.py:'To execute the ai rquality file and show the datas 
- 'sudo python3 main.py :' To execute both files and show in the ThingsBoard
### Ensure you have the necessary permissions to access system resources.

## ThingsBoard access

- sudo service thingsboard start
### Web UI using the following link:

- http://l0.172.117.104:8080/
## Requirements
- Raspberry Pi with the necessary sensors and actuators.
- Python 3.x installed on your Raspberry Pi.

