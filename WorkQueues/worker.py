# Consumidor
import pika, sys, os, time


def main():
    # Realizar la conexion
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Creacion de la Pila
    channel.queue_declare(queue='hello')




    # Funcion que recibe los mensajes
    """
    Sin el auto_ack=True

    Usando este código podemos estar seguros de que incluso si se mata a un trabajador 
    usando CTRL+C mientras estaba procesando un mensaje, no se perderá nada.
    Poco después de que el trabajador muera, todos los mensajes no reconocidos 
    se volverán a entregar.
    """

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        time.sleep(body.count(b'.'))
        print(" [x] Done")


    # Decirle a RabbitMQ que la funcion recibira
    channel.basic_consume(queue='hello', 
                        on_message_callback=callback, 
                        auto_ack=True)

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

