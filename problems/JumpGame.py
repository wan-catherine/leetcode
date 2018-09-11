class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == [0] or 0 not in nums:
            return True
        return self.solve(nums)

    def solve(self, nums):
        i = len(nums) - 2
        l = []
        while i >= 0:
            if nums[i] >= len(nums) - i - 1:
                l.append(i)
            i -= 1

        if 0 in l:
            return True
        elif len(l) == 0:
            return False
        else:
            while len(l) > 0:
                j = l.pop()
                return self.solve(nums[:j+1])