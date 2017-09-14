def qsort(l):
    if l == []:
        return []
    else:
        f = l[0]
        smaller = qsort([i for i in l[1:] if i < f])
        bigger = qsort([i for i in l[1:] if i >= f])
        return smaller + [f] + bigger


if __name__=='__main__':
    seq=[5,6,78,9,0,-1,2,3,-65,12]
    print(qsort(seq))