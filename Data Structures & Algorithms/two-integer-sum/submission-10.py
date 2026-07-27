class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        length = len(nums)
        r = length
        for l in range(length):
            for r in range(length -1,0,-1):
                if l == r: continue
                if nums[l] + nums[r] == target :
                    return [l,r]
                else:
                    continue
        return []