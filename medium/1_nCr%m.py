class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dp = [[0]*(B+1) for _ in range(A+1)]

        for n in range(A+1):
            for r in range(min(n,B)+1):
                if r == 0 or r == n:
                    dp[n][r] = 1
                else:
                    dp[n][r] = (dp[n-1][r] + dp[n-1][r-1])%C 
        return dp[A][B]%C