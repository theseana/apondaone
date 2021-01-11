import time


counter = 10

while True:
    time.sleep(1)
    print(counter)
    counter -= 1
    if counter == -1:
        break