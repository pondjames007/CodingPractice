# TIPS:
# * searching range can only be 2 to sqrt(n)
# * all the multiples are not the answer
# * use SET will be super slow

class Solution:
    def countPrimes(self, n: int) -> int:
           
        if n<=2: return 0 
    
        res=[True]*n
        res[0]=res[1]=False

        k=int(math.sqrt(n))+1

        for p in range(2,k,1):
            if res[p]==True:
                for i in range(p*2, n,p):
                    res[i]=False

        return sum(res)
