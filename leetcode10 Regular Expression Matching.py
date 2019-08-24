
# In this problem, we assume that there is no "." or "*" in s, the p does not start with "*",
    # there won't be consecutive '*'s in p, the * can only eliminate one preceding char;
# "*" can also propagate the preceding char for one or more times

# For continuous cloning process, consider test cases like: 'bbbbb & b*', 'bbbcb & b*'.

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == None or p == None:
            return False

        m, n = len(s), len(p)
        dp = [[False for j in xrange(n + 1)] for i in xrange(m + 1)]
        dp[0][0] = True

        # see if p[:j] matches s[:0]. This is also to cope with case like s = "aab", p = "c*a*b" so it
            # has an initial state to populate from
        for j in xrange(2, n + 1, 2):
            if p[j - 1] == '*':
                dp[0][j] |= dp[0][j - 2]

        # s only contains a - z, so no need to worry about '*' or '.'
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # note that there won't be 2 '*'s in a row
                elif p[j - 1] == '*':
                    # matches zero char; e.g., 'a*' matches 'a'
                    dp[i][j] |= dp[i][j - 1]
                    if j >= 2:
                        # offset the previous char
                        dp[i][j] |= dp[i][j - 2]
                        # use '*' to proceed 1 more char in s while p pointer stays put
                        if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                            dp[i][j] |= dp[i - 1][j]

        return dp[-1][-1]



print Solution().isMatch('bbbbb', 'b*')
print Solution().isMatch('bbbcbb', 'b*')
print Solution().isMatch('mississippi', 'mis*is*p*.')
print Solution().isMatch('av', '.*')





