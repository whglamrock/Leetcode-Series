
'''
idea came from: https://leetcode.com/discuss/15790/share-my-o-log-min-m-n-solution-with-explanation
'''

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            return

        imin, imax, half_len = 0, m, (m+n+1)/2

        while imin <= imax:
            i = (imin+imax)/2
            j = half_len-i

            if j > 0 and i < m and B[j-1] > A[i]: # i is too small, must increase it
                imin = i + 1
            elif i > 0 and j < n and A[i-1] > B[j]:  # i is too big, must decrease it
                imax = i - 1
            else:   # i is perfect
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])

                if (m+n)%2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right)/2.0



Sol = Solution()
print Sol.findMedianSortedArrays([1,2,3,4,5],[6,7,8,9,10,13])




