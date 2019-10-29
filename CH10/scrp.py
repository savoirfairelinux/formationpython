import time 
import threading 
from multiprocessing import Queue  
import requests 

class Consumer(threading.Thread): 
    def __init__(self, queue): 
        threading.Thread.__init__(self)
        self._queue = queue 

    def run(self):
        while True: 
            content = self._queue.get() 
            if isinstance(content, str) and content == 'quit':
                break
            response = requests.get(content)
        print('Thanks!')


def Producer():
    urls = [
    'http://www.python.org', 'http://www.yahoo.com',
    'http://www.scala.org', 'http://www.google.com',
    ]
    queue = Queue()
    worker_threads = build_worker_pool(queue, 4)
    start_time = time.time()

    # Add the urls to process
    for url in urls: 
        queue.put(url)  
    # Add the poison pill
    for worker in worker_threads:
        queue.put('quit')
    for worker in worker_threads:
        worker.join()
    time_print = time.time() - start_time
    print('Done! Time taken: {time_print}')

def build_worker_pool(queue, size):
    workers = []
    for _ in range(size):
        worker = Consumer(queue)
        worker.start() 
        workers.append(worker)
    return workers

if __name__ == '__main__':
    Producer()