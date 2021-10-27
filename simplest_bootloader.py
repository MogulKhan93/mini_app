import time

a = ['\\', '|', '/', '—']

while True:
    for i in a:
        print(i, end='')
        time.sleep(0.3)
        print('\r', end='')
