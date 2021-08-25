import random
import string

def generate_randid():
    chars = string.digits + string.ascii_uppercase
    chars = chars.replace('I', '')
    chars = chars.replace('O', '')

    return ''.join(random.choice(chars) for i in range(8))
