class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        result = []
        for i in range(A):
            row = [1]  # First element in each row is always 1
            for j in range(1, i + 1):
                # Calculate each element based on the previous row
                element = row[j - 1] * (i - j + 1) // j
                row.append(element)
            result.append(row + [0] * (A - len(row)))  # Fill with zeros after actual values
        return result