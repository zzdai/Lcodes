#!/usr/bin/env python
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        g = []
        cnt = 1
        for i in xrange(N-1):
            if s[i] == s[i+1]:
                cnt += 1
            else: 
                g.append(cnt)
                cnt = 1
        g.append(cnt)
        N = len(g)
        cnt = 0
        for i in xrange(N-1):
            cnt += min(g[i],g[i+1])

        """
        for i in xrange(N-1):
            print "i:", i
            if not s[i] == s[i+1]:
                switch = 1
                pk = 1
            if s[i] == s[i+1] and switch == 0:
                cnt1 += 1
            if not s[i] == s[i+1] and switch == 1:
                switch = 0
                cnt2 = cnt1
                cnt1 = 0
            print "cnt1:",cnt1
            print "cnt2:",cnt2

        for i in xrange(N-1):
            p = s[i] - s[i+1]
            if p == 0:
                cnt += 1
            if p == -1:
                cnt_.append(cnt)
                cnt = 0
            if p == 1:
                cnt_.append(cnt)
                cnt = 0
        L = len(cnt_)
        for i in xrange(L-1):
            if i % 2 
            == 0:
                a0 = (max(a0,min(cnt_[i],cnt_[i+1])+1))
            else:
                a1 = (max(a1,min(cnt_[i],cnt_[i+1])+1))
        """
        return cnt

x = Solution()
s = "01000001110010"
s1 = "00110011"
s2 = "10101"
print(x.countBinarySubstrings(s1))
print(x.countBinarySubstrings(s2))
