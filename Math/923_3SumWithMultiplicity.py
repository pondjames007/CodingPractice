# TIPS:
#
# use itertools.combinations_with_replacement
# 3 possible conditions:
# i == j == k
# i == j != k
# i < k and j < k
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        c = collections.Counter(A)
        res = 0
        
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j != k: res += c[i] * (c[i] - 1) // 2 * c[k]
            elif k > i and k > j: res += c[i] * c[j] * c[k]
        
        return res % (10**9 + 7)