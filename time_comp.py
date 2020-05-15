





#Time complexity analasis indicated in code comments 


class Solution:
  def fairCandySwap(self, A, B):
    #an assignment O(1)  
    delta = (sum(B) - sum(A)) // 2
    # and assignment O(1)
    S = set(B)
    # searches through the array with a time complexity of O(N)
    for a in A:
      if a + delta in S:
        #return
        return [a, a + delta]

#Total time compleixty overall is O(N) == O(1)*O(1)*O(N)



solution = Solution()
print(solution.fairCandySwap([1,1],[2,3]))



