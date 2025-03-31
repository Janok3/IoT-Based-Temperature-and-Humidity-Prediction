
# Temperature and Humidity Prediction with SNN Using Real Time Data

In this project we will use a RaspberryPi with a DHT11 sensor to get the real time temperature and humidity. This data will be used to train an SNN model that will give predictions on the temperature and humidity. All of the data so far will be sent to a ThingSpeak channel to later be sent to an MQTT client through the use of Node-Red.
## Setting Up the RaspberryPi
- Make sure the RaspberryPi is connected to your computer via a LAN cable.
- Go to your network adapter settings, then choose the RaspberryPi connection. In the properties, under "Internet Protocol Version 4" set the IP as 10.0.0.1 and the subnet mask as 255.0.0.0.
- Under network adapter settings again, select your private network. Under properties, then sharing, make sure to tick both boxes.

## Connecting to RaspberryPi
There are two ways you can connect to the RaspberryPi:
### 1. Using PuTTY:
- Open PuTTY, enter hostname 10.0.0.2, enter a name and save.
- Click "Accept" on the "PuTTY Sec Alert" window that pops up.
- Enter the username and password of your RaspberryPi ("pi" for both in our case).
### 2. Using VNC:
- After ignoring the sign-in in window, enter 10.0.0.2 in the VNC connect bar and enter the username and password of your RaspberryPi ("pi" for both in our case).

## Running the SNN Network
Once you are connected to the RaspberryPi, make sure you have the necessary python libraries installed by running this command: 
```
pip install Adafruit_DHT numpy requests
```
If you encounter an issue, you may need to install one more package with this command:
```
pip install adafruit-circuitpython-dht
```

After installing the necessary packages you need to set the variables for write_api_key and channel_id in the python program, "SNN.py".

## Setting Up ThingSpeak
- Create a new channel and give it a name. 
- Select 4 fields and name them accordingly ("Predicted Temperature", "Predicted Humidity", "Temperature" and, "Humidity" in our case). 
- Take note of the Channel ID, Write API Key and Read API Key. 
## Setting Up Node-Red
- Run Node-Red by typing "node-red" in CMD.
- Follow the link given at the bottom of the output.
- Import the given "flow.json" file by clicking on the three lines at the top right side, import and, selecting the file.
- After importing the flow, make sure to go into the "http request" node and paste the modified version of this URL with your channel ID and your read API key.
```
https://api.thingspeak.com/channels/{YOUR_CHANNEL_ID}/feeds.json?api_key={YOUR_READ_API_KEY}&results=2
```
## Setting Up MQTT
* Open your preferred MQTT software (MQTT.fx in our case). 
* Enter "test.mosquitto.org" for the URL and "1883" for the port.
* Press "Connect".
* Go to the "Subscribe" tab and subscribe to the following: 
  * /predTemp
  * /predHum
  * /temp
  * /hum


## Running the Program
Once all of the previous steps have been completed, the program is ready to run. 

- Start off by running the SNN.py program in the RaspberryPi, you should see the data start to appear in the "Private View" tab in ThingSpeak.
- Next, deploy the Node-Red flow by pressing "deploy" on top right.

After these steps, the data should be visible in the MQTT client.
### Contributors
Janok N. Dinçer
Çağan Çakır 
