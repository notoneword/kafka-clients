from kafka import KafkaConsumer
import json

def consume_messages():
  print("Start consume_messages")
  consumer = KafkaConsumer(
  bootstrap_servers='broker:9092',
  #  security_protocol="SSL",
  #  ssl_cafile="./ca.pem",
  #  ssl_certfile="./service.cert",
  #  ssl_keyfile="./service.key",
  value_deserializer = lambda v: json.loads(v.decode('ascii')),
  auto_offset_reset='earliest'
  )
  print("consumer defined, subscribing . . .")

  consumer.subscribe(topics='hello_world')
  for message in consumer:
    print ("%d:%d: v=%s" % (message.partition,
                            message.offset,
                            message.value))

if __name__ == "__main__":
    consume_messages()