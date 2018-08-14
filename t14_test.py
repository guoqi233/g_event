from gevent import monkey; monkey.patch_socket()
import gevent
import socket
import time


def func(_id):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8888))
    s.setblocking(True)
    # print s.recv(32).strip()
    s.close()
    # print("{} is done!".format(_id))


def main():
    threads = [gevent.spawn(func, i) for i in range(8192)]
    map(lambda x: x.start(), threads)
    gevent.joinall(threads)


if __name__ == '__main__':
    start = time.time()
    main()
    print time.time() - start
