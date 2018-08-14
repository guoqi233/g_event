import gevent
import random
import time
from gevent import Greenlet


class MyGreenlet(Greenlet):
    def __init__(self, msg):
        super(MyGreenlet, self).__init__()
        self.msg = msg

    def _run(self):
        gevent.sleep(random.randint(0, 2) ** 0.01)
        # print("Task id {} done".format(self.msg))
        pass


def echo(msg):
    print(msg)


def test():
    th = gevent.spawn(echo, "hello")
    print(isinstance(th, Greenlet))


def main():
    threads = [MyGreenlet(i) for i in range(102400)]
    map(lambda x: x.start(), threads)
    gevent.joinall(threads)
    # g = MyGreenlet(1)
    # g.start()
    # g.join()


if __name__ == '__main__':
    start = time.time()
    main()
    print time.time() - start
