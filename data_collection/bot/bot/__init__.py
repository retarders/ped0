__version__ = '0.1.0'

import omegalul
import argparse
import sqlite3
import threading
import time
import random

queue = []

def update_db(database_path, queue):

    with sqlite3.connect(database_path) as connection:

        messages = [(message['id'], message['chat'], message['content'], message['time']) for message in queue]

        connection.executemany('INSERT INTO messages values (?, ?, ?, ?)', messages)
        connection.commit()

def open_chat(message):
    chat_id = random.randint(1111111, 9999999)
    
    chat = omegalul.create_chat()
    chat.start()

    print('{}: id {}'.format(chat_id, chat.id))

    chat.message(message, wpm=20)
    print('{}: sent {}'.format(chat_id, message))

    for i in range(20):
        time.sleep(2)

        events = chat.get_events()

        if events:
            for event in events:
                if event[0] == 'gotMessage':
                    print('{}: received {}'.format(chat_id, event[1]))
                    id = random.randint(1111111, 9999999)

                    queue.append({
                        'id': id,
                        'chat': chat_id,
                        'content': event[1],
                        'time': int(time.time())
                    })

    chat.stop()

def chat_loop(message):
    while True:
        open_chat(message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('message', type=str, default='F15', help='First message to send (may have newlines and will be split into multiple messages)')
    parser.add_argument('database', type=str, help='Location to SQLite3 database')
    parser.add_argument('chats', type=int, help='Number of concurrent chats')

    args = parser.parse_args()

    for i in range(args.chats):
        threading.Thread(target=chat_loop, args=[args.message]).start()

    while True:
        time.sleep(3)

        if not len(queue) == 0:
            update_db(args.database, queue)
            queue = []

