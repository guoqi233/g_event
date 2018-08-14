import gevent
from gevent.queue import Queue, Empty


tasks = Queue(maxsize=3)


def worker(n):
    try:
        while True:
            task = tasks.get(timeout=1)
            print("Worker {0} task {1}".format(n, task))
            gevent.sleep(1)
    except Empty:
        print("Quitting")


def boss():
    for i in xrange(10):
        tasks.put(i)

    print("Asigend all work in interation 1")
    for i in xrange(10, 20):
        tasks.put(i)
    print("Assigned all work in internation 2")


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(boss),
        gevent.spawn(worker, "steve"),
        gevent.spawn(worker, "john"),
        gevent.spawn(worker, "alice"),
    ])

