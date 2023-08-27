#
# @lc app=leetcode id=338 lang=python
#
# [338] Counting Bits
#

# @lc code=start
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0]
        for i in range(1, n + 1):
            if i % 2 == 1:
                dp.append(dp[i - 1] + 1)
            else:
                dp.append(dp[i // 2])
        return dp
# @lc code=end
