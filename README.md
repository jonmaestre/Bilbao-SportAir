# IoT Project - Bilbao SportAir

This repository hosts the complete source code and documentation for the Bilbao SportAir project, a comprehensive IoT solution developed as part of the IoT course. The project's primary focus is on environmental monitoring, specifically targeting temperature, humidity, and air quality metrics. This solution is particularly tailored for deployment in urban environments like Bilbao, where monitoring such parameters is crucial for maintaining a healthy, active lifestyle.

## Repository Contents

- `temhumTBCopia.py:` Python script dedicated to the acquisition and processing of temperature and humidity data. This script interfaces with appropriate sensors connected to a Raspberry Pi, retrieves environmental data, and processes it for further use.

- `airqualityTBCopia.py:` This script is responsible for gathering and handling air quality data. Similar to the temperature and humidity script, it interacts with air quality sensors attached to the Raspberry Pi, ensuring accurate and real-time data acquisition.

- `main.py:` The central script of the project, orchestrating the functions of the above scripts. It manages the workflow, ensuring seamless data collection, processing, and transmission to the designated platforms like ThingsBoard.

## Usage Instructions

To get started with the Bilbao-SportAir project, follow these steps:

1. **Clone Repository on Raspberry Pi:**

   ```bash
   git clone https://github.com/jonmaestre/Bilbao-SportAir.git
   cd Bilbao-SportAir
   ```

2. **Modify Scripts:**
   
   Open and adjust the scripts as per your project requirements using the nano editor:
   
   ```bash
   nano temhumTBCopia.py
   nano airqualityTBCopia.py
   nano main.py
   ```
   
   Make the necessary modifications and save the changes.

3. **Run the Scripts:**

   Execute the individual or main script based on your requirement:
   
   ```bash
   sudo python3 temhumTBCopia.py # Executes the temperature script
   sudo python3 airqualityTBCopia.py # Executes the air quality script
   sudo python3 main.py # Executes both scripts and displays data in ThingsBoard
   ```
   
   Ensure you have the necessary permissions to access system resources.

4. **ThingsBoard Access:**

   Start the ThingsBoard service and access the Web UI:
   
   ```bash
   sudo service thingsboard start
   ```
   
   Access the Web UI using the following link:
   
   `http://10.172.117.104:8080/`

## System Requirements

- Raspberry Pi (with Raspbian OS or similar) equipped with necessary sensors and actuators for temperature, humidity, and air quality measurement.
- Python 3.x installed on your Raspberry Pi.

## Additional Content

- **Web Application:**
  
  For a comprehensive view of the data, we've developed a Web Application. You can download it as 'Web Bilbao_SportAir_Version.zip'. Open the 'index.html' to access the full features of the webpage, which provides a user-friendly interface for data visualization and analysis.

- **Community Support:**

  We encourage community involvement and contributions. If you have suggestions for improvements or have developed additional features, please feel free to share them with the community by submitting pull requests or opening issues.

## Project Vision

Our vision with Bilbao-SportAir is to empower communities with real-time environmental data, fostering awareness and promoting healthier lifestyles. By making this technology accessible and easy to use, we aim to contribute to the broader goal of sustainable and smart city development.
