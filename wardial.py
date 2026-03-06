'''
This is a lab for CSCI040.
Complete the lab by fixing the FIXME annotations below.
'''

import requests


def is_server_at_hostname(hostname):
    '''
    A hostname is a generic word for either an IP address or a domain name.
    Your function should return True if `requests.get` is successfully able to connect to the input hostname.

    >>> is_server_at_hostname('google.com')
    True
    >>> is_server_at_hostname('www.google.com')
    True
    >>> is_server_at_hostname('GoOgLe.CoM')
    True
    >>> is_server_at_hostname('142.250.68.110')  # IP address for google.com
    True

    >>> is_server_at_hostname('facebook.com')
    True
    >>> is_server_at_hostname('www.facebook.com')
    True
    >>> is_server_at_hostname('FACEBOOK.com')
    True

    >>> is_server_at_hostname('google.commmm')
    False
    >>> is_server_at_hostname('aslkdjlaksjdlaksjdlakj')
    False
    >>> is_server_at_hostname('142.250.68.110.1.3.4.5')
    False
    >>> is_server_at_hostname('8.8.8.8')
    False
    '''
    try:
        requests.get('http://' + hostname, timeout=5)
        return True
    except requests.exceptions.RequestException:
        return False


def increment_ip(ip):
    '''
    Return the "next" IPv4 address.

    >>> increment_ip('1.2.3.4')
    '1.2.3.5'
    >>> increment_ip('1.2.3.255')
    '1.2.4.0'
    >>> increment_ip('0.0.0.0')
    '0.0.0.1'
    >>> increment_ip('0.0.0.255')
    '0.0.1.0'
    >>> increment_ip('0.0.255.255')
    '0.1.0.0'
    >>> increment_ip('0.255.255.255')
    '1.0.0.0'
    >>> increment_ip('0.255.5.255')
    '0.255.6.0'
    >>> increment_ip('255.255.255.255')
    '0.0.0.0'
    '''
    parts = [int(x) for x in ip.split('.')]

    parts[3] += 1
    if parts[3] > 255:
        parts[3] = 0
        parts[2] += 1
    if parts[2] > 255:
        parts[2] = 0
        parts[1] += 1
    if parts[1] > 255:
        parts[1] = 0
        parts[0] += 1
    if parts[0] > 255:
        parts[0] = 0

    return f'{parts[0]}.{parts[1]}.{parts[2]}.{parts[3]}'


def enumerate_ips(start_ip, n):
    '''
    Return a list containing the next `n` IPs beginning with `start_ip`.

    >>> list(enumerate_ips('192.168.1.0', 2))
    ['192.168.1.0', '192.168.1.1']

    >>> list(enumerate_ips('8.8.8.8', 10))
    ['8.8.8.8', '8.8.8.9', '8.8.8.10', '8.8.8.11', '8.8.8.12', '8.8.8.13', '8.8.8.14', '8.8.8.15', '8.8.8.16', '8.8.8.17']

    >>> list(enumerate_ips('192.168.0.255', 2))
    ['192.168.0.255', '192.168.1.0']

    >>> len(list(enumerate_ips('8.8.8.8', 10)))
    10
    >>> len(list(enumerate_ips('8.8.8.8', 1000)))
    1000
    >>> len(list(enumerate_ips('8.8.8.8', 100000)))
    100000
    '''
    ip = start_ip
    for _ in range(n):
        yield ip
        ip = increment_ip(ip)


if __name__ == '__main__':
    # Safe placeholder range for testing program structure only.
    test_ips = list(enumerate_ips('127.0.0.0', 16))

    ips_with_servers = []
    for ip in test_ips:
        print('scanning', ip)
        if is_server_at_hostname(ip):
            ips_with_servers.append(ip)

    print('ips_with_servers=', ips_with_servers)
    