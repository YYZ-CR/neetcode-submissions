class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #holds indices of bars until one that's smaller comes. should be listed in increasing order
        largest = 0
        d = len(heights)
        for i in range(d):
            while stack and heights[i] < heights[stack[-1]]:
                h = stack.pop()
                if not stack: #if that was the last element (ie smallest so far):
                    largest = max(heights[h]*i, largest)
                else:
                    largest = max((i-stack[-1]-1)*heights[h], largest)
            stack.append(i)
        while stack:
            h = stack.pop()
            if not stack:
                largest = max(heights[h]*d, largest)
            else: 
                largest = max((d-stack[-1]-1)*heights[h], largest)
        return largest


