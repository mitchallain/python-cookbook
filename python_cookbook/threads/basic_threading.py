from time import sleep
from threading import Thread


def task():
    sleep(1)
    print('This is from another thread')


if __name__ == "__main__":
    thread = Thread(target=task)
    thread.start()
    print('Waiting for the thread...')
    thread.join()
