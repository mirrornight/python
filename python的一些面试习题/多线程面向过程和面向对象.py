# coding=utf-8
import threading
import time
import os

def doChore():
    time.sleep(0.5)

# def booth(tid):
    # global i
    # global lock
    # while True:
        # lock.acquire()
        # if i != 0:
            # i = i - 1
            # print tid, ':now left:', i
            # doChore()
        # else:
            # print 'Thread_id', tid, 'No more tickets'
            # os._exit(0)
        # lock.release()
        # doChore()

# i = 100
# lock = threading.Lock()

# for k in range(10):
    # new_thread = threading.Thread(target = booth, args = (k,))
    # new_thread.start()

print 'hello'
class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid = tid
        self.monitor = monitor
        threading.Thread.__init__(self)
    # 通过修改Thread类的run()方法来定义线程所要执行的命令
    def run(self):
        while True:
            monitor['lock'].acquire()
            if monitor['tick'] != 0:
                monitor['tick'] = monitor['tick'] - 1
                print self.tid, ':now left:', monitor['tick']
                doChore()
            else:
                print 'Thread_id', self.tid, 'No more tickets'
                os._exit(0)
            monitor['lock'].release()
            doChore()

monitor = {'tick': 20, 'lock': threading.Lock()}

for k in range(10):
    new_thread = BoothThread(k, monitor)
    new_thread.start()
    # join()方法，调用该方法的线程将等待直到改Thread对象完成，再恢复运行。
    #new_thread.join()

























