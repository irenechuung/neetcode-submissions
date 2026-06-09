class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = dict()
        for n in nums:
            numToFreq[n] = numToFreq.get(n, 0) + 1
        
        # sort by frequency descending, take first k keys
        sorted_nums = sorted(numToFreq, key=lambda x: numToFreq[x], reverse=True)
        return sorted_nums[:k]