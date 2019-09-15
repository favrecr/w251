import paho.mqtt.client as mqtt
from ibm_botocore.client import Config
import ibm_boto3
import time

cos_credentials={
  "apikey": "",
  "endpoints": "",
  "iam_apikey_description": "",
  "iam_apikey_name": "",
  "iam_role_crn": "",
  "iam_serviceid_crn": "",
  "resource_instance_id": ""
}

auth_endpoint = 'https://iam.bluemix.net/oidc/token'
service_endpoint = 'https://s3.sjc.us.cloud-object-storage.appdomain.cloud'

cos = ibm_boto3.resource('s3',
                         ibm_api_key_id=cos_credentials['apikey'],
                         ibm_service_instance_id=cos_credentials['resource_instance_id'],
                         ibm_auth_endpoint=auth_endpoint,
                         config=Config(signature_version='oauth'),
                         endpoint_url=service_endpoint)
i = 1
def on_message(client, userdata, message):
    global i
    print("message received on IBM VSI subscriber")
    key = 'face' + str(i) + '.png'
    cos.Bucket(name='storagetina').put_object(Key=key, Body=message.payload)
    print("message uploaded to object storage")
    i += 1

# mosquitto broker on IBM VSI docker container
broker_address="172.18.0.2"
# creating new instance of client
client = mqtt.Client("facesubremote")
#attach function to callback
client.on_message=on_message
#connect to broker
client.connect(broker_address,1883)

client.subscribe("remoteface/image")
#wait to process callback
time.sleep(4)

client.loop_forever()