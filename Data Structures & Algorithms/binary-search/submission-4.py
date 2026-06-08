class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom = 0
        top = len(nums)
        l = len(nums)
        while l>0:
            l = (top-bottom)//2
            i = bottom + l
            if target == nums[i]:
                return i
            elif target > nums[i]:
                bottom = i
            elif target < nums[i]:
                top = i
        return -1

            