import gevent


def foo():
    print("Running in foo")
    gevent.sleep(0)
    print("Explicit context switch to foo again")


def bar():
    print("Explict context to bar")
    gevent.sleep(0)
    print("Implcit context switch back to bar")


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar)
    ])

