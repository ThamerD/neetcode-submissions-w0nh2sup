class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        min_q = []
        result = []

        for num in nums:
            frequencies[num] = 1 + frequencies.get(num, 0)
        
        for key, value in frequencies.items():
            heapq.heappush(min_q, (value, key))
            if len(min_q) > k:
                heapq.heappop(min_q)

        for i in range(k):
            result.append(heapq.heappop(min_q)[1])
        return result