import time


def echo(i):
    time.sleep(0.001)
    return i


def fun1():
    from multiprocessing.pool import Pool
    pool = Pool(10)
    run1 = [a for a in pool.imap_unordered(echo, xrange(10))]
    run2 = [a for a in pool.imap_unordered(echo, xrange(10))]
    run3 = [a for a in pool.imap_unordered(echo, xrange(10))]
    run4 = [a for a in pool.imap_unordered(echo, xrange(10))]
    print(run1 == run2 == run3 == run4)


def fun2():
    from gevent.pool import Pool
    pool = Pool(10)
    run1 = [a for a in pool.imap_unordered(echo, xrange(10))]
    run2 = [a for a in pool.imap_unordered(echo, xrange(10))]
    run3 = [a for a in pool.imap_unordered(echo, xrange(10))]
    run4 = [a for a in pool.imap_unordered(echo, xrange(10))]
    print(run1 == run2 == run3 == run4)
    print(run1)


if __name__ == '__main__':
    fun1()
    fun2()
