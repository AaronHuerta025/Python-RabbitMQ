# Consumidor
import pika
import time


# Realizar conexion a la base de datos
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#Declarar la cola
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

# Metodo para recibir los mensajes
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# No da un mensaje de trabajador a la vez
channel.basic_qos(prefetch_count=1)

# A continuación, tenemos que decirle a RabbitMQ que esta 
    # función de devolución de llamada en particular debe recibir 
    # mensajes de nuestra cola de saludos:

channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()