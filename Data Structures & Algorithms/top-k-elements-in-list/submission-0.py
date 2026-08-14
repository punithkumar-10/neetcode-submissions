class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        for num in nums:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1
                
        sorted_dict = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
        
        first_k_items = list(sorted_dict.items())[:k]
        
        result = [item[0] for item in first_k_items]
        return result
