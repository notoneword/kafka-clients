# WIP: Connecting to broker container for topic list, but not yet consuming messages successfully

:::::::::::::::
Notebook init
:::::::::::::::

pip install kafka-python

```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    bootstrap_servers='broker:9092',
       # security_protocol="SSL",
       # ssl_cafile="./ca.pem",
       # ssl_certfile="./service.cert",
       # ssl_keyfile="./service.key",
      value_deserializer = lambda v: json.loads(v.decode('ascii')),
      auto_offset_reset='earliest'
  )

print(consumer.topics())

consumer.subscribe(topics='hello_world')
for message in consumer:  
    print ("In Loop")
    print ("%d:%d: v=%s" % (message.partition,
                            message.offset,
                            message.value))

```


::::::::::
CLI for creating topic, consuming, producing
::::::::::

docker exec broker kafka-topics --bootstrap-server broker:9092 --create --topic hello_world

docker exec --interactive --tty broker kafka-console-producer --bootstrap-server broker:9092 --topic hello_world

docker exec --interactive --tty broker kafka-console-consumer --bootstrap-server broker:9092 --topic hello_world --from-beginning

docker exec broker kafka-topics --bootstrap-server broker:9092 --list



:::::::::::::::::
Logging from jupyter to get UI link:
:::::::::::::::::

To access the server, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/jpserver-6-open.html
    Or copy and paste one of these URLs:
        http://54796b0871df:8888/lab?token=e88a42b8888956c88e861b42261bde1bbee0119bba310220
     or http://127.0.0.1:8888/lab?token=e88a42b8888956c88e861b42261bde1bbee0119bba310220

**Running this on Windows for now, with Docker Desktop**

https://github.com/conduktor/kafka-stack-docker-compose/blob/master/full-stack.yml

Needs make:
:::::::::::::::::
Install make for windows
:::::::::::::::::

https://sourceforge.net/projects/gnuwin32/

#actually have 'make' command

Winget install GnuWin32.make
