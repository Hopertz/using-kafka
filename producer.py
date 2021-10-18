import time
import json
import random
from datetime import datetime
from data_generator import genertate_messages
from kafka import KafkaProducer, producer

# Message will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer = serializer
)

if __name__ == '__main__':
    # Initialize loop - runs untill you kill the program
    while True:
        # Generate a message
        dummy_message = genertate_messages()
        # Send its to ou 'message' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('sms', dummy_message)

        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1,11)
        time.sleep(time_to_sleep)