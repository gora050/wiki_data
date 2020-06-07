import json
import requests
from kafka import KafkaClient, KafkaProducer


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)


def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)


producer = KafkaProducer(bootstrap_servers=["localhost:9092"],  value_serializer=lambda x: json.dumps(x).encode("utf-8"))

r = requests.get("https://stream.wikimedia.org/v2/stream/page-create", stream=True)

for line in r.iter_lines():
    my_json = line.decode('utf8')
    brackets_index = my_json.find(":")
    # my_json = my_json.replace("'", '"')
    if "ok" in my_json or not my_json or "event" in my_json or my_json.startswith("id"):
        continue
    my_json = '{"' + my_json[:brackets_index] + '"' + my_json[brackets_index:] + "}"
    data = json.loads(my_json)
    print(data)
    producer.send('events', data).add_callback(on_send_success).add_callback(on_send_error)

producer.flush()
