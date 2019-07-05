# TIPS:
# map() and zip()
# reverse manipulation of zip()

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        # change num in nums into binary string
        # it will return an instance (iterable), can be "listed" by list()
        bin_string_list = map('{:032b}'.format, nums)
        
        # use zip(*li) to "unzip" each bit
        # each element in the returned list will be the collection of i-th bit from all nums
        # it will return an instance (iterable), can be "listed" by list()
        bit_list = zip(*bin_string_list)
        
        # number of difference in each bit in each pair combination:
        # C(a,1) * C(b,1), a == '0' count, b == '1' count
        return sum(bits.count('0') * bits.count('1') for bits in bit_list)