# TIPS:
# * Use bisect to quickly search the list
# * or implement binary search by yourself

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3: return 0
        
        count = 0
        
        nums.sort()
        
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                c = nums[i] + nums[j]
                k = bisect.bisect_left(nums[j+1:], c)
                count += k
                
        return count
    
# Implement Binary Search
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        lst = sorted(nums)
        
        N = len(lst)
        
        cnt = 0
        for i in range(N-2):
            for j in range(i+1, N-1):
                master = lst[i] + lst[j]
                
                hi = len(lst)
                lo = j + 1
                
                while lo < hi:
                    mid = (lo + hi) // 2
                    
                    if master > lst[mid]:
                        lo = 1 + mid
                    else:
                        hi = mid
                
				# if all c edge candidates are too large, the idx will be (j+1)-1 = j. 
				# So in the following line, the (idx-j) = 0
                idx = lo - 1
                
                cnt += (idx - j)
                
        return cnt