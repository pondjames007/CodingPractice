# TIPS:
# MINMAX Strategy: every one will choose the best moveto them
#
# SOL: Recursion without Memoization
#
# We don't care about the orders that previous numbers were taken IF the game is still ongoning.
# 12X... == 21X... (Since they are not finished yet)
# Total states can be reduced from M! to 2^M (Permutation -> Combination)
# T: O(2^M * M) (O(2^M) subproblems, each problem takes O(M) time)
# S: O(2^M)
#
# 
# Optimization:
# 1. Memoization
# 2. Use 1 byte to store a solution
# 3. Use an integer to represent the numbers used (Bit Operation) 
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal: return False
        if desiredTotal <= 0: return True
        
        # every bit represents a number is chosen or not, so we got 2^M long mem
        # 1001 -> number 1 and 4 are chosen
        # the value in mem is state: 0 = unknown, 1 = can win, -1 = can not win
        mem = [0]*(1 << maxChoosableInteger)
        
        return self.game(maxChoosableInteger, desiredTotal, mem, 0)
    
    def game(self, M, T, mem, chosen_pattern):
        # if T is already <= 0: it means that the game is over and you lose
        if T <= 0: return False
        
        # if the pattern has been simulated, return the ans
        # if the ans == 1 -> can win, return True
        # if the ans == -1 -> cannot win, return False
        if mem[chosen_pattern]: return mem[chosen_pattern] == 1 

        # Go through all possible numbers
        for i in range(M):
            if chosen_pattern & (1<<i): continue # number i+1 used

            # If the next player can not win, current player wins
            if not self.game(M, T - (i+1), mem, chosen_pattern | (1<<i)):
                mem[chosen_pattern] = 1
                return mem[chosen_pattern]
        
        # if all branches cannot win, then mark the branch as -1
        mem[chosen_pattern] = -1
        return False