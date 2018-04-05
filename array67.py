#!/usr/bin/env python 

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return '{:b}'.format(int(a,2)+int(b,2))

x = Solution()
a = "11"
b = "1"
print(x.addBinary(a,b))
