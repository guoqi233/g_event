from threading import Thread
from multiprocessing import Process
import random
import time


class MyThread(Process):
    def __init__(self, msg):
        super(MyThread, self).__init__()
        self.msg = msg

    def run(self):
        time.sleep(random.randint(0, 2) ** 0.01)
        # print("Task id {} done".format(self.msg))


def main():
    threads = [MyThread(i) for i in range(102400)]
    map(lambda x: x.start(), threads)
    map(lambda x: x.join(), threads)


if __name__ == '__main__':
    start = time.time()
    main()
    print time.time() - start
