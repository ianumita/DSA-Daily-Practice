"""
Problem: Two Sum
Approach: Brute Force
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = len(nums)
        for i in range(l):
            for y in range(i+1,l):
                x = nums[i]+nums[y]
                if x == target:
                    return [i, y]
