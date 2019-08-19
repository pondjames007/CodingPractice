# TIPS:
# 99% the same as base2
# for base2: keep divide 2^M until N == 1 or 0
# in code: N & 1 to see if the last digit is 0 or 1, then N >> 1 right shift until N is finished
# for base -2, keep divide -2^M -> in code: add '-' for every right shift
class Solution:
    def baseNeg2(self, N: int) -> str:
        ans = []
        while N:
            ans.append(N & 1)
            N = -(N >> 1)
            
        return ''.join(map(str, ans[::-1] or [0]))