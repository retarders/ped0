import json
import random
from typing import List
from .chat import Chat
from . import session

servers: List[str] = []

def create_chat() -> Chat:
    sess = session.create_session()

    if not servers:
        servers = json.loads(api.status(sess))['servers']

    server = random.choice(servers)

    id = randid.generate_randid()

    return Chat(sess, server, id)
