class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for i in operations:
            sr_len=len(score)-1
            if i=="+" and len(score)>0:    
                score.append(score[sr_len]+score[sr_len-1])
            elif i=="D" and len(score)>0:
                score.append(2*score[sr_len])
            elif i=="C" and len(score)>0:
                score.pop(-1)
            else:
                score.append(int(i))
        return sum(score)
