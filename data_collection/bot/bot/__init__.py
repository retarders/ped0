__version__ = '0.1.0'

import omegalul
import argparse
import sqlite3
import threading

def update_db(database_path, queue):

    with sqlite3.connect(database_path) as connection:

        messages = [(message['chat'], message['content'], message['time']) for message in queue]

        connection.executemany('INSERT INTO messages values (?, ?, ?)', messages)

def open_chat(message):
    chat = omegalul.create_chat()
    chat.start()

    chat.disconnect()

if __name__ == '__main__':
    queue = []

    parser = argparse.ArgumentParser()
    parser.add_argument('message', type=int, default='F15', help='First message to send (may have newlines and will be split into multiple messages)')
    parser.add_argument('database', type=str, help='Location to SQLite3 database')
    parser.add_argument('chats', type=int, help='Number of concurrent chats')

    args = parser.parse_args()

    for i in range(args.chats):
        threading.Thread(target=open_chat, args=[args.message]).start()

    while queue:
        update_db(args.database, queue)
        queue = []
