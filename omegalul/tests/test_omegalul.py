from omegalul import __version__
import omegalul

def test_version():
    assert __version__ == '0.1.0'

def test_start():
    chat = omegalul.create_chat()

    assert chat.id

    try:
        chat.stop()
    except:
        pass
