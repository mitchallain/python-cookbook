import queue
import logging
import threading
import time


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


# https://stackoverflow.com/questions/35160417/threading-queue-working-example
class QueueWorker(threading.Thread):
    def __init__(self, work_queue: queue.Queue, *args, **kwargs):
        self.work_queue = work_queue
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            try:
                work = self.work_queue.get(timeout=3)
            except queue.Empty:
                return

            logger.info("Working on %s", work)
            self.work_queue.task_done()


def main():
    work_queue = queue.Queue()

    for item in range(100):
        work_queue.put_nowait(item)

    for _ in range(20):
        QueueWorker(work_queue).start()

    work_queue.join()  # blocks until the queue is empty.


if __name__ == "__main__":
    main()
