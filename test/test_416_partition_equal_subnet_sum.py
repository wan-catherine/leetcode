from unittest import TestCase
from problems.N416_Partition_Equal_Subnet_Sum import Solution

class TestSolution(TestCase):
    def test_canPartition(self):
        self.assertEqual(True, Solution().canPartition([1,5,11,5]))

    def test_canPartition_1(self):
        self.assertEqual(False, Solution().canPartition([1,2,3,5]))

    def test_canPartition_2(self):
        self.assertEqual(False, Solution().canPartition([1,2,5]))

    def test_canPartition_3(self):
        self.assertEqual(True, Solution().canPartition([23,13,11,7,6,5,5]))
