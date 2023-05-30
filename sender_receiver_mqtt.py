import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc)+"\n")
    client.subscribe("test/topic/up1072668")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

client.loop_start()

while True:
    message = input("\nEnter message: ")
    client.publish("test/topic/up1072668", message)

client.loop_stop()












