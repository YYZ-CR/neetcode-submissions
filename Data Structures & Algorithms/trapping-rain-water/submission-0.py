class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        tallest = 0
        area = 0
        while l<r:
            tallest = max(tallest, min(height[l], height[r]))
            if height[l] <= height[r]:
                area += tallest-height[l]
                l += 1
            elif height[l] > height[r]:
                area += tallest-height[r]
                r -= 1
        return area
