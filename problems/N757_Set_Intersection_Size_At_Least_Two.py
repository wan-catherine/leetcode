class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = set()
        first, second = None, None
        for i, j in intervals:
            if second == None or i > second:
                second = j
                first = second - 1
                res.add(first)
                res.add(second)
                continue
            if i <= first and j >= second:
                continue
            if i > first:
                first, second = second, j
                res.add(first)
                res.add(second)
        return len(res)





