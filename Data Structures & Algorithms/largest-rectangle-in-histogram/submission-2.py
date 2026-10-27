class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        leftside=[-1]*len(heights)
        stack=[]
        maxArea=0

        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()

            if stack:
                leftside[i]=stack[-1]
            stack.append(i)

        
        rightside=[len(heights)]*len(heights)
        stack=[]
     

        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()

            if stack:
                rightside[i]=stack[-1]
            stack.append(i)

        for i in range(len(heights)):
            leftside[i]+=1
            rightside[i]-=1
            maxArea=max(maxArea, heights[i]*(rightside[i]-leftside[i]+1))
        return maxArea
              