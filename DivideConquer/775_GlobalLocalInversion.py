# TIPS:
# Goal can be simplified as: return Flase if there is a pair (i, j) that j-i > 1 and A[i] > A[j]
# It can be further simplified as: if there are 2 numbers swapped which they are not neighbors -> return False 
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        
        for i in range(len(A)-1):
            if A[i] != i: # A[:i] := i
                if A[i] == i+1 and A[i+1] == i:
                    A[i], A[i+1] = A[i+1], A[i] # swap them back if they are neighbors so that next verification can be right.
                else: return False
        return True