class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num=-1
        for i in range(len(arr)-1,-1,-1):
            curr = arr[i]
            arr[i]=max_num
            if curr>max_num:
                max_num=curr
            
        arr[-1]=-1
        return arr