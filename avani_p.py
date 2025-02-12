import pika


RABBITMQ_HOST = "192.168.122.46"  

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# Declare a queue named 'orders'
channel.queue_declare(queue='orders')

# Publish a message
message = "Hello from Avani's VM2"
channel.basic_publish(exchange='', routing_key='orders', body=message)

print(f" [x] Sent '{message}'")

# Close connection
connection.close()
