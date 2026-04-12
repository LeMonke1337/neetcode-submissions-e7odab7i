class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rank = {}
        for num in nums:
            rank[num] = rank.get(num , 0) + 1 
        top_k = sorted(rank, key=rank.get, reverse=True)[:k]

        return top_k



