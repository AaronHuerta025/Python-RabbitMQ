"""
    Un productor es una aplicación de usuario que envía mensajes.
    Una cola es un buffer que almacena mensajes.
    Un consumidor es una aplicación de usuario que recibe mensajes.


    Hay varios tipos de intercambio disponibles: DIRECT, TOPIC, HEADERS y FANOUT.
     Nos centraremos en el último: el fanout. Vamos a crear un intercambio de ese tipo, y lo llamaremos logs:



"""

# Plublisher


import pika
import sys


# Realizar la conexion con RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declarar el exchange y el tipo de comunicacion
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Declarar el mensaje
message = ' '.join(sys.argv[1:]) or "info: Hello World!"

# Declaracion del Routing Key y el exchange

# Nota si el exchange esta vacio, entonces esta usando un exchange por defecto
"""
El parámetro exchange es el nombre del intercambio. 
La cadena vacía denota el intercambio por defecto o sin nombre: 
los mensajes se dirigen a la cola con el nombre especificado por routing_key, 
si existe.

"""
channel.basic_publish(exchange='logs', 
                        routing_key='', 
                        body=message)

print(" [x] Sent %r" % message)
connection.close()

