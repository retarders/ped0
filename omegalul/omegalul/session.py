import requests
import user_agent

OPERATING_SYSTEMS = ['mac', 'windows', 'iphone', 'android']

def create_session() -> requests.Session:
    """
    Creates a session for all the requests to be sent to Omegle in the
    future. We use a session to persist certain settings about the
    requests such as the User Agent (since we don't want to be sending
    them from the requests.py agent)
    """

    agent = user_agent.generate_user_agent(os=OPERATING_SYSTEMS)
    
    session = requests.Session()
    session.headers['User-Agent'] = agent

    return session
