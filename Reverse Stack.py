from typing import List


class Solution:
    def reverse(self, st):
        # code here
        h = []
        h = st[::-1]
        st.clear()
        for i in h:
            st.append(i)


# {
# Driver Code Starts

# Initial Template for Python 3


for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)