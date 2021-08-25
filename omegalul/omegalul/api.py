import requests

def status(session: requests.Session):
    return session.get('https://omegle.com/status').text

def events(session: requests.Session, server: str, id: str):
    return session.post('https://{}.omegle.com/events'.format(server), data={'id': id})
