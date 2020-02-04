#!/usr/bin/python
import threading
import time

exitFlag = 0

class EpicThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        threadLock.acquire()
        TimeFunc(self.name, self.counter, 4)
        print("Exiting " + self.name)
        threadLock.release()

def TimeFunc(thread, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" %(thread, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

thread1 = EpicThread(1, "Thread Number 1", 1)
thread2 = EpicThread(1, "Thread Number 2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print("Exit Main Thread")
