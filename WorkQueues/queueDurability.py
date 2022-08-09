"""
Cuando RabbitMQ se para o se bloquea, olvidará las colas y los mensajes,
 a menos que le digas que no lo haga. Se necesitan dos cosas para asegurarse 
 de que los mensajes no se pierden: necesitamos marcar tanto la cola como los 
 mensajes como duraderos.

En primer lugar, tenemos que asegurarnos de que la cola sobrevivirá
a un reinicio del nodo RabbitMQ.
Para ello, tenemos que declararla como duradera:
"""

import pika, sys, os, time

# Realizar la conexion
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Nota: Si la cola ya esta creada no podemos agregar parametros nuevos, tendremos que Generar un nueva
channel.queue_declare(queue='task_queue', durable=True)


"""
Este cambio en queue_declare debe aplicarse tanto al código del productor 
como al del consumidor.

En este punto estamos seguros de que la cola task_queue no se perderá 
aunque RabbitMQ se reinicie. Ahora necesitamos marcar nuestros mensajes
 como persistentes - proporcionando una propiedad delivery_mode con el 
 valor de pika.spec.PERSISTENT_DELIVERY_MODE
"""

# channel.basic_publish(exchange='',
#                       routing_key="task_queue",
#                       body=message,
#                       properties=pika.BasicProperties(
#                          delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
#                       ))



"""
Despacho justo

Puede que te hayas dado cuenta de que el despacho 
todavía no funciona exactamente como queremos. Por ejemplo, 
en una situación con dos trabajadores, cuando todos los mensajes 
impares son pesados y los pares son ligeros, uno de los trabajadores 
estará constantemente ocupado y el otro apenas hará trabajo. Pues bien, 
RabbitMQ no sabe nada de eso y seguirá despachando los mensajes de forma uniforme.

Esto sucede porque RabbitMQ sólo despacha un mensaje cuando el mensaje entra en la cola. 
No mira el número de mensajes no reconocidos por un consumidor. Simplemente envía a ciegas
 cada n-ésimo mensaje al n-ésimo consumidor.

Para evitarlo, podemos utilizar el método Channel#basic_qos con el ajuste prefetch_count=1. 
Esto utiliza el método de protocolo basic.qos para decirle a RabbitMQ que no dé más de un mensaje 
a un trabajador a la vez. O, en otras palabras, que no envíe un nuevo mensaje a un trabajador hasta 
que haya procesado y reconocido el anterior. En su lugar, lo enviará al siguiente trabajador que no 
esté todavía ocupado.

"""

# channel.basic_qos(prefetch_count=1)
