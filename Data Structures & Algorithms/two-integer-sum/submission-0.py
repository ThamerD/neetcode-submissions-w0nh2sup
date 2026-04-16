class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_idx = {}

        for i, x in enumerate(nums):
            if (target - x) in value_to_idx:
                return [value_to_idx[target - x], i]
            
            value_to_idx[x] = i
        