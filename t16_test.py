a = None


def func():
    global a
    a = 3
    b = 4
    print globals()
    print locals()


if __name__ == '__main__':
    func()
    print a
