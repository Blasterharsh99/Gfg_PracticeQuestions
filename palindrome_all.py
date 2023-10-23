import pdb
def isPalindrome(a):
    b=str(a)
    #pdb.set_trace()
    b=b[::-1]
    if str(a) == b:
        return True
    else:
        return False
def PalinArray(arr ,n):
    # Code here
    for i in arr:
        if not isPalindrome(i):
            return False
    return True
arr=[111,222,333]

if PalinArray(arr,3):
    print(1)
else:
    print(0)