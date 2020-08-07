def get_greet(name: str):
    return f'Hi, {name}'


def print_hello(name):
    msg = get_greet(name)
    print(msg)


if __name__ == '__main__':
    print_hello('Hello, PyCharm')