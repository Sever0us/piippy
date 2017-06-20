import time

from flask import Flask, jsonify, request

from piippy.identity import get_ip

from werkzeug.contrib.cache import SimpleCache

'''
This module runs the server side software which has three jobs:

1) It collects the identity of any clients on the subnet
2) It acts as a webserver which dispatches a dashboard.
3) It hosts a restful api for the daashboard.
'''

serverApp = Flask(__name__)
cache = SimpleCache()
serverIp = get_ip()


class cached(object):
    '''
    This class acts as a function decorator allowing indivisual routes
    to be cached for a specified period.

    Simply add the decorator with an optional 
    `@cached(timeout=20)`
    '''
    def __init__(self, timeout=20):
        self.timeout = timeout

    def __call__(self, f):
        def decorator(*args, **kwargs):
            response = cache.get(request.path)
            if response is None:
                response = f(*args, **kwargs)
                cache.set(request.path, response, self.timeout)
            return response
        return decorator


@serverApp.route('/api/clients', methods=['GET'])
@cached()
def get_identity():
    return jsonify({'time': time.time()})

@serverApp.route('/api/handshake', methods=['GET'])
def handshake():
    return 'True'

if __name__ == '__main__':
    start_time = time.time()
    serverApp.run(
        host='0.0.0.0',
        port=9600
    )
