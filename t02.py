import time
import gevent
from gevent import select

start = time.time()


def tic():
    return "at %1.1f seconds" % (time.time() - start)


def gr1():
    print("Start Polling: {}".format(tic()))
    select.select([], [], [], 2)
    print("Ended Polling: {}".format(tic()))


def gr2():
    print("Start Polling: {}".format(tic()))
    select.select([], [], [], 2)
    print("Ended Polling: {}".format(tic()))


def gr3():
    print("Hey lets do some stuff while the greenlets poll, {}".format(tic()))
    gevent.sleep(1)
    print("Ended Polling: {}".format(tic()))


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(gr1),
        gevent.spawn(gr2),
        gevent.spawn(gr3),
    ])
