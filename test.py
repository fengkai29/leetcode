def erfe(ary,key):
    low = 0
    high = len(ary)-1
    while low<=high:
        mid = int((low+high)/2)
        if ary[mid] == key:
            return mid
        elif key> ary[mid]:
            low = mid + 1
        else:
            high = low -1
    if low>high:
        return -1

ary = [1,2,3,4,5,6,7]
key = 7
print(erfe(ary,key))