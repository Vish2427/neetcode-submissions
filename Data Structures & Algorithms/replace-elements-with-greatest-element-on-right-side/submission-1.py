class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num=-1
        for i in range(len(arr)-1):
            arr[i]=max(arr[i+1:])
        arr[-1]=-1
        return arr
        return arr