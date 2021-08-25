import requests
import time
from . import api

class Chat:
    """
    A chatting session between two omegle users.
    """

    def __init__(self, session: requests.Session, server: str):
        """
        Construct a new Chat object that holds a chat conversation.

        :param session: The session that holds the consistent User
                        Agent.
        :param server: The omegle server, used as a subdomain for
                       omegle.com.
        """

        self.session = session
        self.server = server

    def message(self, message: str, wpm=0):
        """
        Send message to chat.

        :param message: The message to send.
        :param wpm: Words per minute, this will calculate how much time
                    to wait before actually sending the message to make the stranger
                    feel like the client is real. If it's 0, it will be sent
                    instantly.
        """

        api.typing(self.session, self.server)
        # this is wrong 3000% pls fix nv6
        time.sleep(len(message.split(' ')) * (wpm / 60))
