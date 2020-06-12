from kafka import KafkaConsumer
from json import loads
import requests
from time import sleep
import json

consumer = KafkaConsumer(
    'events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    max_poll_records=20)

message_num = 0
events_list = list()
for message in consumer:
    message_schema = dict()
    new_message = message.value['data']
    message_schema['page_uri'] = new_message['meta']['uri']
    message_schema['page_wiki_id'] = new_message['meta']['id']
    message_schema['page_domain'] = new_message['meta']['domain']
    message_schema['page_wiki_id_num'] = new_message['page_id']
    message_schema['page_title'] = new_message['page_title']
    message_schema['page_creation_timestamp'] = new_message['meta']['dt']
    date = new_message['performer'].get("user_registration_dt")
    user_id = new_message['performer'].get("user_id")
    message_schema['page_author'] = {"wiki_user_id": user_id,
                                     "wiki_user_text": new_message['performer']['user_text'],
                                     "wiki_user_groups": new_message['performer']['user_groups'],
                                     "wiki_user_is_bot": new_message['performer']['user_is_bot'],
                                     "wiki_user_registration_dt": date}
    events_list.append(message_schema)
    message_num += 1
    if message_num == 300:
        # requests.post('http://0.0.0.0:8090/pages/', json=events_list)
        with open("sample.json", "w") as write_file:
            json.dump(events_list, write_file, indent=4)
        print("Batch end")
        sleep(2)
        message_num = 0
        events_list.clear()
