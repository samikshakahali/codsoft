import random
import string

def gen_paswrd(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


try:
    user_length = int(input("Enter desired length: "))
    if user_length < 8:
        print("Password length should be at least 8.")
    else:
        generated = gen_paswrd(user_length)
        print(f"Generated Password: {generated}")
except ValueError:
    print("Please enter a valid password!")
