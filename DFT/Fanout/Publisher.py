import pika, sys


# Publicador
# Realizar la conexion con RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()



# Declarar la cola
numberQueue= input("""Elija la queue a la que desea enviar mensaje:
1.- Q21
2.- Q22
3.- Q23

::""")


queues={
    '1':{
        'queue':'Q21',
        'routing_key': 'X2_Q21'
    },
    '2':{
        'queue':'Q22',
        'routing_key': 'X2_Q22'
    },
    '3':{
        'queue':'Q23',
        'routing_key': 'X2_Q23'

    },
}


# Declarar el exchange y el tipo de comunicacion
channel.exchange_declare(exchange='X2', exchange_type='fanout', durable=True)


# Declarar el mensaje
message = ' '.join(sys.argv[1:]) or "info: Hello World!"



channel.basic_publish(exchange='X2', 
                        routing_key=queues[numberQueue]['routing_key'], 
                        body=message,
                        properties=pika.BasicProperties(delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE))

print(" [x] Sent %r" % message)
connection.close()
