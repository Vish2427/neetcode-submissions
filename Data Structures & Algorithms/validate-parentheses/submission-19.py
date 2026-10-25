class Solution:
    def isValid(self, s: str) -> bool:
        map={
            ")":"(",
            "]":"[",
            '}':"{"
        }
        
        pope=[]
        for i in s:
            if i in map.keys():
                if pope and pope[-1]==map[i]:
                    pope.pop()
                else:
                    return False
            else:
                pope.append(i)
        if len(pope)==0:
            return True
        else:
            return False
            