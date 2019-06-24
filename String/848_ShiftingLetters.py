# TIPS:
# * Use zip()
# * process shifts[] first -> get total sum for each element

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        for idx in range(len(shifts)-2, -1, -1):
            shifts[idx] += shifts[idx+1]
            shifts[idx]
        char = [ord(x)-ord('a') for x in S]
        
        res = [chr((a+b)%26+ord('a')) for a , b in zip(shifts, char)]         
        
        ans = ''.join(res)
        
        return ans