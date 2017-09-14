# coding=utf-8
# import multiprocessing 

# def proc1(pipe):
    # pipe.send('hello')
    # print 'procl rec:', pipe.recv()

# def proc2(pipe):
    # print 'proc2 rec:', pipe.recv()
    # pipe.send('hello, too')

# if __name__ == '__main__':
    # pipe = multiprocessing.Pipe()
    # p1 = multiprocessing.Process(target = proc1, args = (pipe[0],))
    # p2 = multiprocessing.Process(target = proc2, args = (pipe[1],))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

#===================================================================
import os
import multiprocessing
import time

def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.time())
    queue.put(info)

def outputQ(queue, lock):
    info = queue.get()
    # 这些进程共享一个stdout 
    lock.acquire()
    print str(os.getpid()) + '(get):' + info
    lock.release()
  
record1 = []
record2 = []
 
if __name__ == '__main__': 
    
    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue(3)
    for i in range(10):
        process = multiprocessing.Process(target = inputQ, args = (queue,))
        process.start()
        record1.append(process)

    for i in range(10):
        process = multiprocessing.Process(target = outputQ, args = (queue, lock))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    queue.close()
    for p in record2:
        p.join()


























