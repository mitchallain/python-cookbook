from time import sleep
from threading import Thread, current_thread


class CustomThread(Thread):
    def __init__(self):
        super().__init__()
        self.value = 0

    def run(self):
        sleep(1)
        print(f"This is coming from the thread {self.name}")
        self.value = 10


thread = CustomThread()
thread.start()
print(f"Got value {thread.value}")
print(f"Waiting for the thread {thread.name} to finish")
thread.join()
print(f"Got value {thread.value}")

thread = current_thread()
print(f"Current thread is {thread.name}")
