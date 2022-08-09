# Consumidor 
import pika



try:
    # Realizar la conexion con RabbitMQ
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()

    # Declarar el exchange y el tipo de comunicacion
    channel.exchange_declare(exchange='X3', exchange_type='topic', durable=True)

    # Declarar la cola
    numberQueue= input("""Elija la queue a la que desea consumir:
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



    channel.queue_declare(queue=queues[numberQueue]['queue'], durable=True)

    # Hacer el binding de la cola y el exchange
    channel.queue_bind(exchange='X3', queue=queues[numberQueue]['queue'], routing_key=queues[numberQueue]['routing_key'])

    print(' [*] Waiting for logs. To exit press CTRL+C')

    # Funcion que resive los mensajes
    def callback(ch, method, properties, body):
        print(" [x] %r" % body)

    # Decirle a RabbitMQ que la funcion recibira
    channel.basic_consume(
    queue=queues[numberQueue]['queue'], on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


except KeyboardInterrupt:
    print('Consumidor interrumpido')




