class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap=defaultdict(int)
        for i in s:
            hmap[i] +=1
        for j in t:
            hmap[j] -=1

        for k in hmap:
            if hmap[k]!=0:
                return False
        return True