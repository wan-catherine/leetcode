from unittest import TestCase
from problems.N1707_Maximum_XOR_With_An_Element_From_Array import Solution

class TestSolution(TestCase):
    def test_maximizeXor(self):
        self.assertListEqual([3,3,7], Solution().maximizeXor(nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]))

    def test_maximizeXor_1(self):
        self.assertListEqual([15,-1,5], Solution().maximizeXor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]))

    def test_maximizeXor_2(self):
        nums = [760625198, 15138539, 61033, 267654046, 133000577, 229497, 155443, 109330, 13340119, 8260519, 981126373,
         441631490, 498767021, 171522247, 503991705, 11276686, 176397, 23247190, 472734721, 243117401]
        queries = [[383815038, 1000000000], [4194304, 1000000000], [633072806, 981082380], [875344070, 965383924],
         [31380566, 64633365], [4194304, 91884], [4194304, 158853440], [10839453, 224610550], [4194304, 349538162],
         [171815678, 403214196], [15355179, 1000000000], [938931463, 441640682], [23207682, 1000000000],
         [4194304, 1000000000], [75686235, 1000000000], [86208917, 259012], [905942425, 1000000000],
         [692399970, 1000000000], [22418605, 1000000000], [369403291, 1000000000]]
        self.assertListEqual([1001829712,976932069,1072246692,1041598465,31424324,4255337,128806273,178019674,263459742,231792511,982548942,1037028800,991482855,976932069,1056452030,86220796,1069985118,927949563,992794696,995270069], Solution().maximizeXor(nums, queries))

    def test_maximizeXor_3(self):
        self.assertListEqual([815495216,982236586,841545292,298223816,765573696], Solution().maximizeXor([33554432,765021065,42883,293499083,1000000000]
,[[568658171,1000000000],[17921962,1000000000],[162675788,1000000000],[12122115,534140862],[3731913,847670022]]))