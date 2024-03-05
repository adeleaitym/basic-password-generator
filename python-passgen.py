import random # the library that gives the ability to create a random output given an input
import string # this library gives more complexity when generating a password

def generate_password(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range (length))
    return password

password = generate_password()
print(f"Generated password: {password}")
