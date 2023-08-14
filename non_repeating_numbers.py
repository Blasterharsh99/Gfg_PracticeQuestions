class Solution:
	def singleNumber(self, nums):
         singles = set()
         for num in nums:
            if num not in singles:
                singles.add(num)
            else:
                singles.remove(num)
         return sorted(list(singles))



#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()
