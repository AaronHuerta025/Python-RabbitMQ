import pika, sys


# Publicador
# Realizar la conexion con RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()



# Declarar la cola
numberQueue= input("""Elija la queue a la que desea enviar mensaje:
1.- Q31
2.- Q32
3.- Q33

::""")


queues={
    '1':{
        'queue':'Q31',
        'routing_key': 'X3_Q31'
    },
    '2':{
        'queue':'Q32',
        'routing_key': 'X3_Q32'
    },
    '3':{
        'queue':'Q33',
        'routing_key': 'X3_Q33'

    },
}


# Declarar el exchange y el tipo de comunicacion
channel.exchange_declare(exchange='X3', exchange_type='topic', durable=True)


# Declarar el mensaje
message = ' '.join(sys.argv[1:]) or "info: Hello World!"



channel.basic_publish(exchange='X3', 
                        routing_key=queues[numberQueue]['routing_key'], 
                        body=message,
                        properties=pika.BasicProperties(delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE))

print(" [x] Sent %r" % message)
connection.close()
