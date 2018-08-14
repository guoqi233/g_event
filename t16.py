import gevent
from gevent.local import local

stash = local()


def f1():
    setattr(stash, "x", 1)
    print(getattr(stash, "x", None))


def f2():
    setattr(stash, "y", 2)
    print(getattr(stash, "y", None))

    try:
        getattr(stash, "x")
    except AttributeError:
        print("x is not local to f2")


if __name__ == '__main__':
    gevent.joinall(map(lambda x: gevent.spawn(x), [f1, f2]))
