from urllib.request import urlopen

import gevent
import time

def f(url):
    print("URL:%s"%url)
    resp = urlopen(url)
    data = resp.read()

    # with open("tingting.html",'wb') as file:
    #     file.write(data)
    print("%d bytes received from %s."%(len(data),url))

# f("http://www.xiaohuar.com/")
# f("https://www.tingtingfm.com/")
start = time.time()
print("Start:%s"%str(start))
gevent.joinall([
    gevent.spawn(f,"https://www.python.org"),
    gevent.spawn(f,"https://www.yahoo.com"),
    gevent.spawn(f,"https://github.com"),
])
print("End:%s"%str(time.time() - start))