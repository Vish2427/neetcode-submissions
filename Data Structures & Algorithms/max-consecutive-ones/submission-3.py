import math 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx,cnt=0,0
        for num in nums:
            if num==0:
                mx= max(mx,cnt)
                cnt=0
            else:
                cnt=cnt+1
        return max(mx,cnt)


        