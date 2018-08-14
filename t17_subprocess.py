import gevent
from gevent.subprocess import Popen, PIPE


def cron():
    while True:
        print("Cron")
        gevent.sleep(0.2)


if __name__ == '__main__':

    p = Popen("sleep 1;uname", stdout=PIPE, shell=True)
    g = gevent.spawn(cron)
    p.wait()
    g.kill()
    print(p.stdout.read().rstrip())
