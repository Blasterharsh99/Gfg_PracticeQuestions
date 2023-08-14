class Solution:
    def missingNumber(self, array, n):
        # code here
        l = []
        for i in range(1, n + 1):
            l.append(i)
        x = list(set(l) - set(array))
        s = 0
        for j in x:
            s = j
        return s


# {
# Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    s = Solution().missingNumber(a, n)
    print(s)