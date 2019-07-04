# TIPS:
# Binary Search
# it is important to choose side (FLAG is important)
# OOXOO and OOOXOOO should choose different side according to the number of left/right is odd or even

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        i, j = 0, len(nums)-1
        
        while i+2 != j:
            mid = (i+j)//2
            # if mid is even (left/right is even number)
            # choose the side that equal to nums[mid]
            # 
            # if mid is odd (left/right is odd number)
            # choose the side that not equal to nums[mid]
            flag = True if mid%2 == 0 else False
            
            if nums[mid] == nums[mid-1]:
                if flag:
                    j = mid
                else:
                    i = mid+1
            elif nums[mid] == nums[mid+1]:
                if flag:
                    i = mid
                else:
                    j = mid-1
            else:
                return nums[mid]
        
        if nums[i] == nums[i+1]: return nums[i+2]
        else: return nums[i]
        