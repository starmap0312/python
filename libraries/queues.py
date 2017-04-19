# Python Queue: a thread-safe FIFO implementation
# 1) queue: FIFO,    ex. q = Queue.Queue()
# 2) stack: LIFO,    ex. q = Queue.LifoQueue()
# 3) priority queue: ex. Queue.PriorityQueue()
#
# Python3 coroutine Queue:
# 1) asyncio.Queue
# 1) asyncio.LifoQueue
# 1) asyncio.PriorityQueue
import Queue

# 1) basic operations:
#    put() and get()
q = Queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())

# 2) priority queue
class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = Queue.PriorityQueue()

q.put(Job(3 , 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1 , 'Important job'))

while not q.empty():
    next_job = q.get()
    print('Processing job: {0}'.format(next_job.description))

# 3) Using Queues with Threads
import time
from threading import Thread
q = Queue.Queue()
num_fetch_threads = 2
feed_urls = [ 'http://www.castsampler.com/cast/feed/rss/guest', ]

def download(i, q):
    while True:
        url = q.get()
        print('{0}: Downloading: {1}'.format(i, url))
        # instead of really downloading the URL, we just pretend and sleep
        time.sleep(i + 2)
        q.task_done()

for i in range(num_fetch_threads):
    worker = Thread(target=download, args=(i, q,))
    worker.setDaemon(True)
    worker.start()

for url in feed_urls:
    q.put(url)

# main thread (block-)waiting
q.join()
