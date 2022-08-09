import pika, sys

# Publicador


# Realizar la conexion con RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()



# Declarar el exchange y el tipo de comunicacion
channel.exchange_declare(exchange='Python_Ex', exchange_type='direct', durable=True)


# Declarar el mensaje
message = ' '.join(sys.argv[1:]) or "info: Hello World!"



channel.basic_publish(exchange='Python_Ex', 
                        routing_key='Python_Key', 
                        body=message)

print(" [x] Sent %r" % message)
connection.close()
