# coding=utf-8
def Binary_Search(l, n):
    high = len(l) - 1
    low = 0
    mid = (high + low) / 2
    # 注意循环条件
    while high >= low:
        if l[mid] < n:
            # 注意将不要直接将low = mid
            low = mid + 1
            mid = (high + low) / 2
        elif l[mid] > n:
            # 注意将不要直接将high = mid
            high = mid - 1
            mid = (high + low) / 2
        else:
            return True
    return False

if __name__ == '__main__':
    l = [1, 4, 12, 45, 66, 99, 120, 444]
    print Binary_Search(l, 12)
    print Binary_Search(l, 1)
    print Binary_Search(l, 13)
    print Binary_Search(l, 444)
