def create_session():
    """
    Creates a session for all the requests to be sent to Omegle in the
    future. We use a session to persist certain settings about the
    requests such as the User Agent (since we don't want to be sending
    them from the requests.py agent)
    """
    pass
