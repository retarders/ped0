import json
import random
from typing import List
from .chat import Chat
from . import session
from . import randid
from . import api
from typing import List

servers: List[str] = []

def create_chat(topics: List[str] = []) -> Chat:
    sess = session.create_session()

    global servers
    if not servers:
        servers = json.loads(api.status(sess).text)['servers']

    server = random.choice(servers)

    id = randid.generate_randid()

    return Chat(sess, server, id, topics=topics)
