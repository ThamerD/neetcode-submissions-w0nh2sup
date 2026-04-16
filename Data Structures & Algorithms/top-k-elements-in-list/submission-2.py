class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        freq_to_num = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            frequencies[num] = 1 + frequencies.get(num, 0)
        
        for key, value in frequencies.items():
            freq_to_num[value].append(key)
        
        for i in range(len(freq_to_num)-1, 0, -1):
            for num in freq_to_num[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
