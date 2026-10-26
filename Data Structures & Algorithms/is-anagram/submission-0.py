class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap={}
        for i in s:
            if i in hmap:
                hmap[i] +=1
            else:
                hmap[i] = 1
        for j in t:
            if j not in hmap:
                return False
            elif j in hmap and hmap[j]>1:
                hmap[j] -=1
            else:
                hmap.pop(j)

        if hmap:
            return False
        else:
            return True