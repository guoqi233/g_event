import gevent
import random


def task(_id):
    gevent.sleep(random.randint(0, 2)**0.01)
    print("Task id {} done".format(_id))


def synchronous():
    for i in range(10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


if __name__ == '__main__':
    print("synchronous")
    synchronous()
    print("synchronous")
    asynchronous()
