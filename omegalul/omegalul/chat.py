import requests
import json
import time
import random
from . import api
from typing import List

class Chat:
    """
    A chatting session between two omegle users.
    """

    def __init__(self, session: requests.Session, server: str, randid: str, topics: List[str] = []):
        """
        Construct a new Chat object that holds a chat conversation.

        :param session: The session that holds the consistent User
                        Agent.
        :param server: The omegle server, used as a subdomain for
                       omegle.com.
        :param randid: The randid parameter.
        """

        self.session = session
        self.server = server
        self.randid = randid
        self.topics = topics
        self.id = ''

    def start(self):
        """
        Starts the chat.
        """

        response = api.start(self.session, self.server, self.randid, topics=self.topics)
        self.id = json.loads(response.text)['clientID']

        return response

    def message(self, message: str, wpm=0):
        """
        Send message to chat.

        :param message: The message to send.
        :param wpm: Words per minute, this will calculate how much time
                    to wait before actually sending the message to make the stranger
                    feel like the client is real. If it's 0, it will be sent
                    instantly.
        """

        api.typing(self.session, self.server, self.id)

        # this is wrong 3000% pls fix nv6
        # time.sleep((60 / wpm) * len(message.split(' ')))

        time.sleep(random.randind(1.0, 3.5))

        api.stopped_typing(self.session, self.server, self.id)

        return api.send(self.session, self.server, self.id, message)

    def get_events(self):
        """
        Synchonously get events.

        WIP.
        """

        events = json.loads(api.events(self.session, self.server, self.id).text)
        return events

    def stop(self):
        """
        Stop the chat by disconnecting.
        """

        return api.disconnect(self.session, self.id, self.server)
