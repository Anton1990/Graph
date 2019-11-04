def rec(a,b):
    if b == 0:
        return 1
    else:
        return a * rec(a, b-1)


    
    


houses = [1,2,3,4,5,6,7,8,9,10]


def isSorted(ary):
    for i in range(1, len(ary)):
        if (ary[i] < ary[i - 1]):
            return False
    return True


def binSearch(arr, elem, l, r):
    if l<=r:
        mid=0
        mid=l+int((r-l)/2)
        if arr[mid]==elem:
            return mid
        elif mid>elem:
            return binSearch(arr, elem, l, mid-1)
        else:
            return binSearch(arr, elem, mid+1, r)
        
    else:
        return -1
   

ary = (1, 2, 3, 4, 5, 6, 7,13)
print (binSearch(ary, 6, 0, len(ary) -1))
