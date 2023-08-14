class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            a, b = 0, 1
            for i in range(2, n + 1):
                c = (a + b) % 1000000007
                a, b = b, c
            return b % 1000000007

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        obj = Solution()
        res = obj.nthFibonacci(n)

        print(res)