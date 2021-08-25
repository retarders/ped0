import requests

def status(session: requests.Session):
    return session.get('https://omegle.com/status').text

def start(session: requests.Session, server: str, randid: str):
    return session.post('https://{}.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid={}&lang=en'.format(server, randid))

def events(session: requests.Session, server: str, id: str):
    return session.post('https://{}.omegle.com/events'.format(server), data={'id': id})

def typing(session: requests.Session, server: str, id: str):
    return session.post('https://{}.omegle.com/typing'.format(server), data={'id': id})

def send(session: requests.Session, server: str, id: str, message: str):
    return session.post('https://{}.omegle.com/send'.format(server), data={
        'id': id,
        'msg': message
    })

def disconnect(session: requests.Session, id: str, server: str):
    return session.post('https://{}.omegle.com/disconnect'.format(server), data={'id': id})
