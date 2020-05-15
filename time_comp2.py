#Time complexity written in code comments

class Solution:
    def isPowerOfTwo(self, n):

        if n == 1: return True
        # assignment O(1)
        power = 0
        # assignment O(1)
        num = 2
        # similar time notation as a for loop (O)N
        while num <= n:
            #O(1)
            if num == n:
                return True
            #(O)N**
            else:
                power += 1
                num = 2**power
            #print(num)
        return False

# Since as O notation inputs and complexity get larger we drop the smaller time complexity the overall time complexit i would give this is 
# O(N)** 
#that O of N squared
solution = Solution()
print(solution.isPowerOfTwo(4))