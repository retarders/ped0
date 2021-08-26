import omegalul
import threading

def events_receiver(chat: omegalul.chat.Chat):
    while True:
        events = chat.get_events()

        if events:
            for event in events:
                if event[0] == 'typing':
                    print('Stranger is typing...')
                if event[0] == 'gotMessage':
                    print(event[1])
                else:
                    print('Invalid event: ' + event[0])
                    print(event)

while True:
    if input('Start chat? [Y/n] ').lower() == 'y':
        chat = omegalul.create_chat()
        chat.start()

        receiver_thread = threading.Thread(target=events_receiver, args=[chat])
        receiver_thread.start()

        print('You are now chatting with someone')
        print('ID: ' + chat.id)
        print('Commands:')
        print('/{exit,quit,disconnect,leave}')
        
        while True:
            message = input('> ')

            if message.startswith('/'):
                if message.split('/')[1] in ['exit', 'quit', 'disconnect', 'leave']:
                    chat.stop()
                    print('Disconnected from the chat')
                    break
            else: 
                chat.message(message, 0)
                print('You: ' + message)

    else:
        break
