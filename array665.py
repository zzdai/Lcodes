#!/usr/bin/env python

#665 Non-decreasing Array

class Solution(object):
	def checkPossibility(self, nums):
		"""
		:type nums: List[int]
		rtype: bool
		"""
		if len(nums) <3:
			return True
		count = 0
		pointer = 0
		for i in xrange(len(nums)-1):
			if nums[i] > nums[i+1]:
				count += 1
				pointer = i
				"""the decreasing point"""
				if count >= 2:
					return False
		if pointer == len(nums)-2 or pointer == 0:
			return True
		if nums[pointer-1] <= nums[pointer+1] or nums[pointer] <= nums[pointer+2]:
			return True
			"""decrease pointer or increase the point after pointer"""
		return False

x = Solution()
nums = [1,2,4,0,3]
print(x.checkPossibility(nums))

