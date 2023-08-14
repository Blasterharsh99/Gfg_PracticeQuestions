# User function Template for python3
from itertools import permutations


class Solution:
    def permutation(self, s):

        n = len(s)
        p = permutations(s)
        k = []
        for i in p:
            l = ""
            for r in range(n):
                l += i[r]
            k.append(l)
        return k


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())
    while (T > 0):
        s = input()
        ob = Solution()
        ans = ob.permutation(s)
        for i in ans:
            print(i, end=" ")
        print()

        T -= 1