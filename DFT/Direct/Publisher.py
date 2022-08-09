import pika, sys


# Publicador
# Realizar la conexion con RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()



# Declarar la cola
numberQueue= input("""Elija la queue a la que desea enviar mensaje:
1.- Q11
2.- Q12
3.- Q13

::""")


queues={
    '1':{
        'queue':'Q11',
        'routing_key': 'X1_Q11'
    },
    '2':{
        'queue':'Q12',
        'routing_key': 'X1_Q12'
    },
    '3':{
        'queue':'Q13',
        'routing_key': 'X1_Q13'

    },
}


# Declarar el exchange y el tipo de comunicacion
channel.exchange_declare(exchange='X1', exchange_type='direct', durable=True)


# Declarar el mensaje
message = ' '.join(sys.argv[1:]) or "info: Hello World!"



channel.basic_publish(exchange='X1', 
                        routing_key=queues[numberQueue]['routing_key'], 
                        body=message,
                        properties=pika.BasicProperties(delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE))



# channel.basic_publish(exchange='X1', 
#                         routing_key=queues[numberQueue]['routing_key'], 
#                         body=message)

print(" [x] Sent %r" % message)
connection.close()
