class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0
        t = len(nums)-1
        while b <= t:
            mid = (b+t)//2
            if b == t:
                if nums[b] == target: 
                    return b
                else: 
                    return -1
            elif nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if (nums[t] > target and nums[t] > nums[mid]) or nums[t] < target or (nums[mid]>=nums[b] and nums[mid]<=nums[t]): #must be in left half
                    t = mid-1
                else: 
                    b = mid+1
            elif nums[mid] < target:
                if (nums[b] < target and nums[b] < nums[mid]) or nums[b] > target or (nums[mid]>=nums[b] and nums[mid]<=nums[t]): # must be in right half
                    b = mid+1
                else:
                    t = mid-1
        return -1