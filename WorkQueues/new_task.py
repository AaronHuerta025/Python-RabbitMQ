# publicador

"""
Por defecto, RabbitMQ enviará cada mensaje al siguiente consumidor,
en secuencia. En promedio, cada consumidor recibirá el mismo número
de mensajes. Esta forma de distribuir los mensajes se llama round-robin.
"""

"""
Si un consumidores comienza una tarea larga y muere con ella sólo 
parcialmente hecha. Con nuestro código actual una vez que RabbitMQ 
entrega el mensaje al consumidor lo marca inmediatamente 
para su eliminación. En este caso, si mata a un trabajador 
perderemos el mensaje que estaba procesando. 




Para asegurarse de que un mensaje nunca se pierde, RabbitMQ soporta acuses de recibo 
de mensajes. Un ack(nowledgement) es enviado de vuelta por el consumidor para decirle 
a RabbitMQ que un determinado mensaje ha sido recibido, procesado y que RabbitMQ es 
libre de borrarlo.


Los acuses de recibo manuales están activados por defecto. En los ejemplos anteriores 
los desactivamos explícitamente mediante la bandera auto_ack=True.
"""




import pika, sys


# Realizar la conexion
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# Declarar la pila
channel.queue_declare(queue='hello')

# Declaracion del mensaje
message = ' '.join(sys.argv[1:]) or "Hello World!"

# Creacion del routing key
channel.basic_publish(exchange='', 
                    routing_key='hello',
                    body=message)



print(" [x] Sent %r" % message)
connection.close()