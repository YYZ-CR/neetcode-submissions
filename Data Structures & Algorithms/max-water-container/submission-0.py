class Solution:
    def maxArea(self, heights: List[int]) -> int:
        big = 0
        l = 0
        r = len(heights)-1
        area = 0
        while r>l:
            area = min(heights[l],heights[r])*(r-l)
            big = max(big, area)
            if heights[r]>heights[l]:
                l += 1
            else:
                r -= 1
        return big
        
        