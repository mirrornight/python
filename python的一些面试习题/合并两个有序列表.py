def f(a, b):
    temp = []
    na = 0
    nb = 0
    while na < len(a) and nb < len(b):
        if a[na] < b[nb]:
            temp.append(a[na])
            na += 1
        elif a[na] > b[nb]:
            temp.append(b[nb])
            nb += 1
        else:
            temp.append(a[na])
            temp.append(b[nb])
            na += 1
            nb += 1
    if na == len(a) and nb < len(b):
        temp = temp + b[nb:]
    elif nb == len(b) and na < len(a):
        temp = temp + a[na:]
    return temp

a = [1, 3, 4, 5, 6, 6]
b = [1, 3, 3 ,5, 8]
print f(a, b)