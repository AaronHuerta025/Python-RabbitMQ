import pika

# Consumer



# Realizar la conexion con RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declarar el exchange y el tipo de comunicacion
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Declarar la cola con nombre aleatorio
# Con el exclusive=True se define una cola temporal
# Si la conexion se va la cola será eliminada
# result = channel.queue_declare(queue='', exclusive=True)
# queue_name = result.method.queue # Contiene el nombre aleatorio
channel.queue_declare(queue='Python')


# Hacer el binding de la cola y el exchange
channel.queue_bind(exchange='logs', queue='Python')

print(' [*] Waiting for logs. To exit press CTRL+C')

# Funcion que resive los mensajes
def callback(ch, method, properties, body):
    print(" [x] %r" % body)

 # Decirle a RabbitMQ que la funcion recibira
channel.basic_consume(
    queue='Python', on_message_callback=callback, auto_ack=True)

channel.start_consuming()