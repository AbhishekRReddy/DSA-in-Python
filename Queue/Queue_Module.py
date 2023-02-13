import queue as q
customQueue = q.Queue(maxsize=5)
print(customQueue.qsize())
customQueue.put(1)
print(customQueue.empty())
print(customQueue.get())