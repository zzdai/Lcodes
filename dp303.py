#!/usr/bin/env python

class NumArray(object):
	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums
		self.accumulate = [0]
		for i in xrange(len(nums)):
			self.accumulate.append(self.accumulate[i]
					+nums[i])
	
	def sumRange(self, i, j):
		"""
		:type i: int	
		:type j: int
		:rtype: int
		"""
		return self.accumulate[j+1]-self.accumulate[i]

nums = [-2,0,3,-5,2,-1]
obj = NumArray(nums)
print(obj.accumulate)
print(obj.sumRange(2,5))
																					          


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
