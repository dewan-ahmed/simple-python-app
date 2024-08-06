# Comment

import os

def hello(name):
    return f"Hello {name}!"

if __name__ == '__main__':
    user_input = input("Enter your name: ")
    # Vulnerability: command injection by allowing user input in os.system
    os.system(f"echo {user_input}")
    print(hello(user_input))
