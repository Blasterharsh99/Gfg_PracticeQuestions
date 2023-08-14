class Solution:
    def sort012(self, arr, n):
        # code here
        d = {0: 0, 1: 0, 2: 0}
        for i in arr:
            d[i] += 1
        arr.clear()

        for i in range(d[0]):
            arr.append(0)
        for i in range(d[1]):
            arr.append(1)
        for i in range(d[2]):
            arr.append(2)
        return arr


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=' ')
        print()