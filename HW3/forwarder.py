import paho.mqtt.client as mqtt 
import time


def on_message(client, userdata, message):
    print("message received on jetson subscriber" ,str(message.payload.decode("utf-8")))
    cloud_client.publish("CloudTopic", message.payload)
    print("message published to cloud ibm vsi topic")

#remote mosquitto broker address on IBM virtual server    
cloud_broker_address="169.53.144.102"
#create new instance of client
cloud_client=mqtt.Client("publishfacetocloud")
#connect to broker
cloud_client.connect(cloud_broker_address, 1883)

#mosquitto broker on jetson docker container
jetson_broker_address="172.18.0.3"
jetson_topic="jetsonimage"
#new instance of client on jetson
client = mqtt.Client("facesubscriber")
#attach function to callback
client.on_message=on_message
#connect to jetson broker
client.connect(jetson_broker_address)


#subscribe to jetson topic
client.subscribe(jetson_topic)
# wait to process callback
time.sleep(4)

client.loop_forever() 




   




