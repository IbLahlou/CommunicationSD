import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue named 'hello'
channel.queue_declare(queue='hello')

# Publish a message to the 'hello' queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello, RabbitMQ!')

print(" [x] Sent 'Hello, RabbitMQ!'")

# Close the connection
connection.close()
