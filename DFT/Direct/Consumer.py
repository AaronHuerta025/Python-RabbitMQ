# Consumidor 
import pika



try:
    # Realizar la conexion con RabbitMQ
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()

    # Declarar el exchange y el tipo de comunicacion
    channel.exchange_declare(exchange='X1', exchange_type='direct', durable=True)

    # Declarar la cola
    numberQueue= input("""Elija la queue a la que desea consumir:
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



    channel.queue_declare(queue=queues[numberQueue]['queue'], durable=True)

    # Hacer el binding de la cola y el exchange
    channel.queue_bind(exchange='X1', queue=queues[numberQueue]['queue'], routing_key=queues[numberQueue]['routing_key'])

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




