class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in nums and nums.index(diff)!=i:
                return [min(i,nums.index(diff)),max(i,nums.index(diff))]