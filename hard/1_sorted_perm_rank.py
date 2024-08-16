class Solution:
	# @param A : string
	# @return an integer
    mod = 1000003
	def fact(self, A):
        if A == 0 or A == 1:
            return 1
        else:
            return (A * self.fact(A-1)) % self.mod

    def findRank(self, A):
        n = len(A)
        ans = 0
        for i in range(n-1):
            count = 0
            for j in range(i+1,n):
                if A[i] > A[j]:
                    count += 1
            pos = n-i-1
            ans += (count*self.fact(pos))%self.mod
        return (ans+1) % self.mod


