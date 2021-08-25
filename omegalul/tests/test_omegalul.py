import omegalul

def test_start():
    chat = omegalul.create_chat()
    chat.start()

    assert chat.id

    try:
        chat.stop()
    except:
        pass
