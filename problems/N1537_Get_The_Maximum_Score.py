class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        repeated_set = set(nums1).intersection(set(nums2))
        repeated_nums = list(repeated_set)
        if not repeated_nums:
            sum1 = sum(nums1)
            sum2 = sum(nums2)
            return sum1 % (10**9 + 7) if sum1 > sum2 else sum2 % (10**9 + 7)

        repeated_nums.sort()
        a, b = [], []
        a_pre, b_pre = 0, 0
        for i in repeated_nums:
            index1 = nums1.index(i)
            a.append(sum(nums1[a_pre:index1]))
            a_pre = index1 + 1

            a.append(i)
            index2 = nums2.index(i)
            b.append(sum(nums2[b_pre:index2]))
            b_pre = index2 + 1
            b.append(i)
        a.append(sum(nums1[a_pre:]))
        b.append(sum(nums2[b_pre:]))
        n = len(a)
        dp = [[0,0] for i in range(n + 1)]
        for i in range(n):
            if i % 2:
                dp[i+1][0] = max(dp[i][0], dp[i][1]) + a[i]
                dp[i+1][1] = max(dp[i][0], dp[i][1]) + a[i]
            else:
                dp[i+1][0] = dp[i][0] + a[i]
                dp[i+1][1] = dp[i][1] + b[i]

        return max(dp[-1][0], dp[-1][1]) %(10**9 + 7)



