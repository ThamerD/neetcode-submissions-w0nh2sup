class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        result = []

        for num in nums:
            frequencies[num] = 1 + frequencies.get(num, 0)
        
        frequencies = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
        
        for key in frequencies:
            if len(result) < k:
                result.append(key)
            else:
                return result

        return result