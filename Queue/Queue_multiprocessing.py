from multiprocessing import Queue
customqueue = Queue(maxsize = 3)
customqueue.put(1)
print(customqueue.get())