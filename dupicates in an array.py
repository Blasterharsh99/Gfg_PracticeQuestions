class Solution:
    def duplicates(self, arr, n):
        d = {}
        l = set(arr)
        x = []
        for i in l:
            d[i] = 0
        for i in arr:
            d[i] += 1
        for i in sorted(l):
            if d[i] > 1:
                x.append(i)
        if len(x) == 0:
            x.append(-1)
            return x
        else:
            return x


# {
# Driver Code Starts
if (__name__ == '__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i, end=" ")
        print()
