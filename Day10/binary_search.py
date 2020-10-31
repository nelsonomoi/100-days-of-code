from bisect import bisect_left

def BinarySearch(a,x):
    i = bisect_left(a,x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1
    
    
a = [1,2,3,4,4,8]
res = BinarySearch(a,9)
if res == -1:
    print("absent")
else:
    print('present')