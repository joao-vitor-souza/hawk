import os

def ping(host):
    print('Ping will start. Press CTRL + C to cancel.')
    os.system(f'ping {host}')


