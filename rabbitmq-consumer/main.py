#!/usr/bin/env python
import pika
import time
import sys
import requests
import bs4

def callback(ch, method, properties, body):
    r = requests.get(body)
    html = bs4.BeautifulSoup(r.text)
    print(html.title)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='lab_queue')

    channel.basic_consume(queue='lab_queue',
                        auto_ack=True,
                        on_message_callback=callback)
    
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


