# Conectarse al servidor de RabbitMQ
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Creacion de una cola
channel.queue_declare(queue='hello')

# Creacion del routing key
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
                      
print(" [x] Sent 'Hello World!'")


# Creacion de una Routing Key
"""
Antes de salir del programa necesitamos asegurarnos de que los buffers de 
red se han vaciado y que nuestro mensaje ha sido realmente entregado a RabbitMQ. 
Podemos hacerlo cerrando suavemente la conexión.
"""
connection.close()
