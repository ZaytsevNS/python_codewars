# Solution for task: https://www.codewars.com/kata/639107e0df52b9cb82720575/

import socket


def socket_client():
    SETTINGS: dict = {'host': '127.0.0.1',
                      'port': 1111,
                     }

    MESSAGE: str = 'Hello, world!'
    
    sock = socket.socket()
    sock.connect((SETTINGS['host'], SETTINGS['port']))
    sock.send(MESSAGE.encode(encoding='utf-8'))
    receives_data = sock.recv(len(MESSAGE)).decode(encoding='utf-8')
    sock.close()
    
    return MESSAGE == receives_data
    