class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #holds indices of bars until one that's smaller comes. should be listed in increasing order
        largest = 0
        d = len(heights)
        for i in range(d):
            while stack and heights[i] < heights[stack[-1]]:
                h = stack.pop()
                if not stack: #if that was the last element (ie smallest so far):
                    area = heights[h]*i
                else:
                    area = (i-stack[-1]-1)*heights[h]
                largest = max(largest, area)
            stack.append(i)
        while stack:
            h = stack.pop()
            if not stack:
                area = heights[h]*d
            else: 
                area = (d-stack[-1]-1)*heights[h]
            largest = max(largest, area)
        return largest


