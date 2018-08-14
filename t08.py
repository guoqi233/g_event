import gevent
from gevent.event import AsyncResult

a = AsyncResult()


def setter():
    gevent.sleep(3)
    a.set("Hello!")


def waiter():
    print("I'm waitting")
    print(a.get())


def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter)
    ])


if __name__ == '__main__':
    main()
