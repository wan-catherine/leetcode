import collections

"""
The key point is to find row1 and row2 which row1 ^ row2 = 1111...11

Flipping a subset of columns is like doing a bitwise XOR of some number K onto each row. 
We want rows X with X ^ K = all 0s or all 1s. This is the same as X = X^K ^K = (all 0s or all 1s) ^ K, 
so we want to count rows that have opposite bits set. 
For example, if K = 1, then we count rows X = (00000...001, or 1111....110)
"""

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        memo = collections.defaultdict(int)
        res = 0
        for row in matrix:
            p, q = [], []
            for i in row:
                p.append(i)
                q.append(1-i)
            str_p, str_q = str(p), str(q)
            memo[str_p] += 1
            memo[str_q] += 1
            res = max(res, memo[str_p], memo[str_q])
        return res


