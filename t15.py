from gevent import sleep
from gevent.pool import Pool
from gevent.lock import BoundedSemaphore

sem = BoundedSemaphore(2)


def worker1(n):
    sem.acquire()
    print("Worker {} acquire semaphone".format(n))
    sleep(0)
    sem.release()
    print("Worker {} releasedsemaphone".format(n))


def worker2(n):
    with sem:
        print("worker {} acquired semaphone".format(n))
        sleep(0)
    print("Worker {} released semaphone".format(n))


pool = Pool()

pool.map(worker2, xrange(3, 6))
pool.map(worker1, xrange(0, 3))
