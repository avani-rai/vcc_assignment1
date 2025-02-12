import pika

RABBITMQ_HOST = "192.168.122.46" 

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# Declare the same queue to receive messages
channel.queue_declare(queue='orders')

# Define a callback function to process received messages
def callback(ch, method, properties, body):
    print(f" [x] Received '{body.decode()}'")

# Start consuming messages from the queue
channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
