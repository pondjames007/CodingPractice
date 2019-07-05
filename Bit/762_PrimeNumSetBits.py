# TIPS:
# Check if it is a prime number:
# go through 2 to n/2, or sqrt(n) or 6k ± 1, with the exception of 2 and 3, and check if it can be divided

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count = 0
        for i in range(L, R+1):
            binary = bin(i)
            set_bits = binary.count('1')
            
            # check n if it is a prime number
            # go through 2 to n/2, or sqrt(2), and check if it can be divided
            if set_bits > 1:
                is_prime = True
                for j in range(2, set_bits//2+1):
                    if set_bits%j == 0:
                        is_prime = False
                        break
                if is_prime:       
                    count += 1
        
        return count