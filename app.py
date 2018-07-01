import requests
import json
import gevent

GEO_LOCATION_API = 'http://ip-api.com/json/?fields=520191&lang=en'

proxies = ['http://176.53.2.122:8080/']

def test_proxy(proxy):
    response = requests.get(GEO_LOCATION_API, proxies={ 'http': proxy })
    print json.loads(response.content)

threads = [gevent.spawn(test_proxy, proxy) for proxy in proxies]
gevent.joinall(threads)
