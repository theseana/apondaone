from threading import Thread
from time import sleep


def timer(t):
    for i in range(t):
        print(i)
        sleep(1)

thread1 = Thread(target=timer, args=(7, ))
thread1.start()

thread2 = Thread(target = timer, args = (8, ))
thread2.start()
