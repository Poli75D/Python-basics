#!/usr/bin/python
import queue
import threading
import time

exitFlag = 0

class EpicThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("Starting " + self.name)
        ProcessData(self.name, self.q)
        print("Exiting " + self.name)

def ProcessData(thread, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (thread, data))

threadList = ["Thread1", "Thread2", "Thread3", "Thread4"]
nameList = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

for tName in threadList:
    thread = EpicThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()

for word in nameList:
    workQueue.put(word)

queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1
    
for t in threads:
    t.join()

print("Exit Main Thread")
