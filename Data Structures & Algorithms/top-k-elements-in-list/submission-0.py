import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        heap = []
        for num, freq in freqs.items():
            heapq.heappush(heap, (-freq, num))

        top_k = [0] * k
        for i in range(k):
            top_k[i] = heapq.heappop(heap)[1]

        return top_k