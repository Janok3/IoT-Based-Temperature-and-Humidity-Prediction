import Adafruit_DHT
import math
import numpy as np
import time
import requests


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

write_api_key = ''  # VPG3IQN4IZPF5WD0
channel_id = ''     # 2857390

inputSize = 2  
hiddenSize = 4  
outputSize = 2

weightsInputHidden = np.array([
    [0.5, -0.3, 0.2, 0.1],
    [-0.4, 0.6, 0.1, 0.3]
    ])

weightsOutputHidden = np.array ([
    [0.1, -0.2],
    [0.2, 0.3],
    [-0.1, 0.4],
    [0.3, -0.1]
])

biasHidden = np.array([0.1, -0.1, 0.05, 0.2])
biasOutput = np.array([0.1, -0.2])

 
def sigmoid(x):
    return 1/(1+np.exp(-x))

 

def predictSNN(temp, hum):
    inputData = np.array([temp, hum])

    hiddenLayer= np.dot(inputData, weightsInputHidden) + biasHidden
    hiddenLayer= sigmoid(hiddenLayer)
 
    outputLayer = (np.dot(hiddenLayer, weightsOutputHidden) + biasOutput)
 
    return outputLayer
 
while True:

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
   
    if humidity is None or temperature is None:
        print("Failed to read from DHT sensor!")
        time.sleep(2)
        continue

    predicted_values = predictSNN(temperature, humidity)
    predicted_temp = predicted_values[0]
    predicted_hum = predicted_values[1]

    print(f"Actual Temp: {temperature:.2f} C, Actual Hum: {humidity:.2f} %")
    print(f"Predicted Temp: {predicted_temp:.2f} C, Predicted Hum: {predicted_hum:.2f} %")

   
    requests.post(f'https://api.thingspeak.com/update?api_key={write_api_key}&field1={predicted_temp}&field2={predicted_hum}&field3={temperature}&field4={humidity}')

    time.sleep(2) 

 