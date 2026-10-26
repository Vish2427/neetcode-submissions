class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap={}
        for i in nums:
            if i in hmap.keys():
                return True
            hmap[i]=1
        return False