class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for i in nums:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1
        
        sortedNums = sorted(frequencies, key=frequencies.get, reverse=True)
            
        return sortedNums[:k]