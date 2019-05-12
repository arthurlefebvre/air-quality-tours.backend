#!/bin/bash
source venv/bin/activate

flask run &

echo $! > pid_backend.txt

python launch_mqtt_broker.py &
echo $! > pid_mqtt.txt

cd frontend

npm run dev 
#echo $! > ../pid_frontend.txt

cd ..

#python launch_mqtt_broker.py &
#$PID = $!
#echo $PID >> list_pids.txt
