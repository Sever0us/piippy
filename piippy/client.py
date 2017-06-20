import time

import requests

from piippy.identity import get_ip, get_mac


def find_server():
    server = None
    a, b, c, d = get_ip().split('.')
    while not server:
        print('Finding server...')
        for i in range(256):
            print(i)
            if test_if_server('.'.join([a, b, c, str(i)])):
                return '.'.join([a, b, c, str(i)])


def test_if_server(hostname):
    try:
        r = requests.get('http://' + hostname + ':9600/api/handshake', 
            timeout=0.1)
    except Exception:
        return False
    if r.text == 'True':
        return True
    return False


if __name__ == '__main__':
    print('Booting service...')
    serverIp = find_server()
    address = 'http://' + serverIp + ':9600/api/log'
    print('Logging...')
    while True:
        time.sleep(10)
        data = {
            'ip': get_ip(),
            'mac': get_mac()
        }
        try:
            requests.post(address, data=data)
            print('Log sent')
        except Exception as e:
            print(e)
