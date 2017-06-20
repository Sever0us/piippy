import socket
from uuid import getnode
'''
This module contains several utility functions for
acquiring machine data such as IP & Mac addresses
'''


def get_ip():
    '''
    Return the assigned IP address for the current machine
    as a string of the form `aaa.bbb.ccc.ddd`
    '''
    return socket.gethostbyname(socket.gethostname())


def get_mac():
    '''
    Return the current machines mac address as a string of
    colon delemited hex e.g. `mm:mm:mm:ss:ss:ss`
    '''
    address = str(hex(getnode()))[2:]
    address = [address[2 * i: 2 * i + 2] for i in range(6)]
    return ':'.join(address)
