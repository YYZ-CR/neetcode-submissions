class Solution:
    def findMin(self, nums: List[int]) -> int:
        b = 0
        t = len(nums)-1
        while b <= t:  
            mid = (b+t)//2
            if nums[b] == nums[t]:
                return nums[b]
            elif nums[mid] < nums[t]: #look in bottom half
                t = mid
            elif nums[mid] > nums[t]: #look in top half
                b = mid + 1
            