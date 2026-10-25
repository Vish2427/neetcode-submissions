class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        text = ''.join([str(i) for i in nums])
        arr=text.split("0")
        max=0
        for i in arr:
            if len(i)>=max:
                max=len(i)
        return max


        