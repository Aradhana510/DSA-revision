Q2. Count of divisors
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description
Given an array of integers A, find and return the count of divisors of each element of the array.

NOTE: The order of the resultant array should be the same as the input array.



Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 106



Input Format
The only argument given is the integer array A.



Output Format
Return the count of divisors of each element of the array in the form of an array.



Example Input
Input 1:

 A = [2, 3, 4, 5]
Input 2:

 A = [8, 9, 10]


Example Output
Output 1:

 [2, 2, 3, 2]
Output 1:

 [4, 3, 4]


Example Explanation
Explanation 1:

 The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
 So the count will be [2, 2, 3, 2].
Explanation 2:

 The number of divisors of 8 : [1, 2, 4, 8], 9 : [1, 3, 9], 10 : [1, 2, 5, 10]
 So the count will be [4, 3, 4].


SOLUTION

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sieve(self,num):
        sieve = [i for i in range(num+1)]
        p = 2
        while p*p <= num:
            if sieve[p] == p:
                for i in range(p*p,num+1,p):
                    if sieve[i] == i:
                        sieve[i] = p
            p += 1
        return sieve

    def  countDivisors(self,num,Arr):

        totalfactors = 1
        while num > 1:
            prime = Arr[num]
            count = 0
            while num%prime == 0:
                count += 1
                num = num//prime
            totalfactors *= (count+1)
        return totalfactors

    def solve(self, A):
        maxx = max(A)
        sieve = self.sieve(maxx)
        res = []
        for num in A:
            res.append(self.countDivisors(num,sieve))
        return res