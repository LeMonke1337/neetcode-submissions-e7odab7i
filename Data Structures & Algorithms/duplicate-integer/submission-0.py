class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_array = len(set(nums))
        return set_array != len(nums)
        