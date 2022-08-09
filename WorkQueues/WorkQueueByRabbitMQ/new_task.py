# Publicador
import pika
import sys

# Realizar conexion a la base de datos
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declarar la cola y marcar su durabilidad para que no se elimine si RabbitMQ se reinicia
channel.queue_declare(queue='task_queue', durable=True)

# Declarar el mensaje
message = ' '.join(sys.argv[1:]) or "Hello World!"

# Declarar el routing key
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    # Marcamos los mensajes como persistentes para que no se pierdan al reiniciar Rabbirt
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))



print(" [x] Sent %r" % message)


connection.close()