
# Time Complixity: O(n)
# Space Complixity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        l = len(nums)
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
