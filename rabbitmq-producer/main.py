#!/usr/bin/env python
import pika
import sys

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='lab_queue')
    urls = ['http://google.com','http://facebook.com']
    for website in urls:
        channel.basic_publish(exchange='',
                    routing_key='lab_queue',
                    body=str(website))

    connection.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


