# TIPS:
# turn the number into binary string
class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        positive = True
        if binary[0] == '0':
            binary = binary[2:]
        else:
            positive = False
            binary = binary[3:]
        
        res = []
        if not positive:   
            res.append('-0b')
        for i in binary:
            if i == '0':
                res.append('1')
            else:
                res.append('0')
                
        
        return int(''.join(res), 2)

# bitwise 
class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        if binary[0] == '0':
            binary = binary[2:]
        else:
            binary = binary[3:]
        
        length = len(binary)
        
        for i in range(length):
            mask = 1 << i
            num ^= mask
        
        return num