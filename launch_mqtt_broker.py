# coding: utf-8
""" Souscription au topic "demo/#" sur le broker Eclipse Mosquitto.
    Utilise une autenthification login/mot-de-passe sur le broker
"""
import paho.mqtt.client as mqtt_client
from time import gmtime, strftime
import datetime
import sqlite3

TOPIC = "AQTours/#"
DB_FILE = "app.db"
DATA_TUPLE = [-1, -1]

# Configuration
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
KEEP_ALIVE = 45  # interval en seconde


def on_log(client, userdata, level, buf):
    print("log: ", buf)


def writeToDb(batiment, salle, temperature, pressure, humidity, IAQ, date):
    print("Entering writeToDb function")
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    print("Writing to db")
    print(salle)
    c.execute('SELECT * FROM room WHERE name=?', (salle,))
    
    salle_id = c.fetchone()[0]
    
    c.execute('INSERT INTO telemetric_data (temperature, pressure, humidity, IAQ, date, room_id) VALUES (?, ?, ?, ?, ?, ?)', [temperature, pressure, humidity, IAQ, date, salle_id])
    conn.commit()

    #c.execute("INSERT INTO temperature VALUES (?,?)",
    #          (currentTime, temperature))
    #conn.commit()


def on_connect(client, userdata, flags, rc):
    print("Connexion: code retour = %d" % rc)
    print("Connexion: Statut = %s" % ("OK" if rc == 0 else "échec"))
    client.subscribe(TOPIC)


def on_message(client, userdata, message):
    print("Reception message MQTT...")
    [projet, batiment, salle] = message.topic.split('/')
    data = message.payload
    print(data)
    date = datetime.datetime.now()
    [temperature, pressure, humidity, IAQ] = data.split('/')
    print(temperature)
    print("Calling writeToDb")
    writeToDb(batiment, salle, temperature, pressure, humidity, IAQ, date)


# Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
client = mqtt_client.Client(client_id="client007")

# Assignation des fonctions de rappel
client.on_message = on_message
client.on_connect = on_connect
#client.on_log = on_log

# Connexion broker
client.username_pw_set(username="aqtours", password="DII42019")
client.connect(host=MQTT_BROKER, port=MQTT_PORT, keepalive=KEEP_ALIVE)
# client.subscribe( "demo/#" )

# Envoi des messages
client.loop_forever()
