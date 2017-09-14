import multiprocessing

# def f(x):
    # return x **2

# if __name__ == '__main__':
    # pool = multiprocessing.Pool(5)
    # rel = pool.map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # print rel

#======================================================================
# def f(n, a):
    # n.value = 3.14
    # a[0] = 5

# if __name__ == '__main__':
    # num = multiprocessing.Value('d', 0.0)
    # arr = multiprocessing.Array('i', range(10))

    # p = multiprocessing.Process(target = f, args = (num, arr))
    # p.start()
    # p.join()
    
    # print num.value
    # print arr[:]
#=======================================================================

def f(x, arr, l):
    x.value = 3.14
    arr[0] = 5
    l.append('Hello')

if __name__ == '__main__':
    server = multiprocessing.Manager()
    x = server.Value('d', 0.0)
    arr = server.Array('i', range(10))
    l = server.list()

    proc = multiprocessing.Process(target = f, args = (x, arr, l))
    proc.start()
    proc.join()

    print x.value
    print arr
    print l


























