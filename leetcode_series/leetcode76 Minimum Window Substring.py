
# remember the idea of 'missing' and 'need'
# edge case: t doesn't exist in s

from collections import Counter

class Solution(object):
    def minWindow(self, s, t):

        if not s or not t:
            return ''

        # i will always be the index of first valid char in a valid window
        i = 0
        I = J = 0
        need, missing = Counter(t), len(t)

        # j will always be the index of last valid char in a valid window (so the window = s[i:j + 1])
        for j, char in enumerate(s):

            # means we found a needed char;
            # when need[char] <= 0, the char could also be in t, it is just we don't need it (the window
            #   has redundant chars)
            if need[char] > 0:
                missing -= 1    # we don't touch missing after it reaches 0

            # need[char] always "-=1" even when the char is in t (e.g., when need[char] == -1, it means
            #   the window has one redundant this char)
            need[char] -= 1

            # means the window either has exactly the number of each char we need or has redundant chars
            if missing == 0:
                # the first condition -- "i < j" is enough, because the "t is empty" scenario has been ruled out
                #   i <= j is also okay, though
                while i < j and need[s[i]] < 0:  
                    need[s[i]] += 1
                    i += 1

                # this if condition should be under the above big if condition because we
                #   only update the I, J when we have a valid window (missing == 0)
                if J == 0 or (j + 1) - i < J - I:
                    J, I = j + 1, i

        # initialize J = 0 and setting the J as j + 1 also fits the condition that t doesn't exist in s
        return s[I:J]



Sol = Solution()
s = 'abdcewgaw'
t = 'abc'
print Sol.minWindow(s, t)
