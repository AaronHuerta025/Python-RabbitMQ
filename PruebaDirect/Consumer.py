# Consumidor 


import pika

# Realizar la conexion con RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declarar el exchange y el tipo de comunicacion
channel.exchange_declare(exchange='Python_Ex', exchange_type='direct', durable=True)

# Declarar la cola
channel.queue_declare(queue='Python_queue', durable=True)


# result = channel.queue_declare(queue='', exclusive=True)
# queue_name = result.method.queue # Contiene el nombre aleatorio




# Hacer el binding de la cola y el exchange
channel.queue_bind(exchange='Python_Ex', queue='Python_queue', routing_key='Python_Key')

print(' [*] Waiting for logs. To exit press CTRL+C')

# Funcion que resive los mensajes
def callback(ch, method, properties, body):
    print(" [x] %r" % body)

# Decirle a RabbitMQ que la funcion recibira
channel.basic_consume(
queue='Python_queue', on_message_callback=callback)

channel.start_consuming()