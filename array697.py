#!/usr/bin/env python

class Solution(object):
	def findShortestSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		first,second,count = {},{},{}
		for index, num in enumerate(nums):
			if num not in first: first[num] = index
			second[num] = index
			count[num] = count.get(num,0)+1

		degree = max(count.values())
		ans = len(nums)
		for num in count:
			if count[num] == degree:
				print(second[num])
				print(first[num])
				ans = min(ans,second[num]-first[num]+1)
		return ans

x = Solution()
#nums1 = [1,2,2,3,1]
nums2 = [1,2,2,3,1,4,2]
#print(x.findShortestSubArray(nums1))
print(x.findShortestSubArray(nums2)) 
