from gevent.pool import Pool
from gevent.server import StreamServer


def handler(socket, address):
    # print socket, address
    socket.send("hello world\r\n")
    socket.close()


pool = Pool(1024)
server = StreamServer(("0.0.0.0", 8888), handle=handler, spawn=pool)
server.serve_forever()
