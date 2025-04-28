
from pika import ConnectionParameters, BlockingConnection

connection_params = ConnectionParameters(
    host="localhost",
    port=5672,
)

def process_message(ch, method, properties, body):
    print(f" получено {body.decode()}")

    ch.basic_ack(delivery_tag=method.delivery_tag)



def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue="messages")

            ch.basic_comsume(
                queue="messages",
                on_message_callback=process_message,

            )
            ch.start_consuming()


            print("zhdy messagi")



if __name__ == "__main__":
    main()




