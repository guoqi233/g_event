from gevent import monkey; monkey.patch_socket()

import gevent
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


def get(ip, _id):
    session = requests.Session()
    session.post("https://{}/rest/Sessions".format(ip), json=dict(UserName="USERID", Password='PASSW0RD'), verify=False)
    req = session.get("https://{}/json/health_temperature".format(ip))
    print(req.status_code)
    # results = req.json()["temperature"]
    # for result in results:
    #     if "inlet" in result["label"].lower():
    #         print result["currentreading"]
    #     elif "exhaust" in result["label"].lower():
    #         print result["currentreading"]
    #     else:
    #         return
    print("Process {} done".format(_id))


def synchronous():
    for i in range(5):
        get("172.20.12.49", i)


def asynchronous():
    threads = list()
    for i in range(5):
        threads.append(gevent.spawn(get, "172.20.12.49", i))
    gevent.joinall(threads)


if __name__ == '__main__':
    print("synchronous")
    synchronous()
    print("synchronous")
    asynchronous()

