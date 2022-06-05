import config.cinfig_main


def print_hi(name):
    print(f'Hi, {name}')
    print(config.cinfig_main.a)
    print([config.cinfig_main.a]*5)


if __name__ == '__main__':
    print_hi('PyCharm')
