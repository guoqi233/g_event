import gevent
from gevent.queue import Queue

tasks = Queue()


def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print("Worker {0} got task {1}".format(n, task))
        gevent.sleep(0)

    print("Quitting time")


def boss():
    for i in xrange(25):
        tasks.put_nowait(i)


if __name__ == '__main__':
    gevent.spawn(boss).join()
    gevent.joinall(map(lambda x: gevent.spawn(worker, x), [item for item in ["steve", "john", "alice"]]))

