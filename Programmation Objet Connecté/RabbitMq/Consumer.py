import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the 'hello' queue again in case it doesn't exist
channel.queue_declare(queue='hello')

# Define a callback function to handle incoming messages
def callback(ch, method, properties, body):
    print(" [x] Received:", body)

# Start consuming messages from the 'hello' queue
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
