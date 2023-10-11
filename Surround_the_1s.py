class Solution:
    def Count(self, matrix):
        count = 0
        for i in range(n):
            for j in range(m):
                l = []
                if matrix[i][j] == 1:
                    if i-1>=0 and j -1>= 0 and i+1<n and j+1<m:
                        l.append(matrix[i - 1][j])
                        l.append(matrix[i - 1][j - 1])
                        l.append(matrix[i][j - 1])
                        l.append(matrix[i - 1][j + 1])
                        l.append(matrix[i + 1][j + 1])
                        l.append(matrix[i + 1][j])
                        l.append(matrix[i][j + 1])
                        l.append(matrix[i + 1][j - 1])
                        c = l.count(0)
                        if c % 2 == 0:
                            count += 1
                    elif i-1<0:
                        pass


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.Count(matrix)
        print(ans)
