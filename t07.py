import gevent
from gevent.event import Event

evt = Event()


def setter():
    gevent.sleep(3)
    print("I'm ok")
    evt.set()


def waiter():
    print("I'll wait for you")
    evt.wait()
    print("Ok, I'm done")


def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
    ])


if __name__ == '__main__':
    main()
