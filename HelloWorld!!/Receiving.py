# CLIENTE

# Conectarse al servidor de RabbitMQ
import pika
import os
import sys

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Generar la cola
    """
    Nota: Si ya esta creada no pasara nada
    """
    channel.queue_declare(queue='hello')


    # Funcion CallBack para recivir los mensajes
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)





    # A continuación, tenemos que decirle a RabbitMQ que esta 
    # función de devolución de llamada en particular debe recibir 
    # mensajes de nuestra cola de saludos:

    channel.basic_consume(queue='hello',
                        auto_ack=True,
                        on_message_callback=callback)


    # Entramos en un bucle interminable que espera datos y ejecuta callbacks
    #  siempre que sea necesario, y captura KeyboardInterrupt durante el cierre del programa.

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


