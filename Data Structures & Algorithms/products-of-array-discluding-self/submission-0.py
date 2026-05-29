class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        prefix = 1
        for i in range(0,len(nums)-1): #prefix
            prefix *= nums[i]
            output[i+1] *= prefix
        suffix = 1
        for i in range(len(nums)-1,0,-1): #suffix
            suffix *= nums[i]
            output[i-1] *= suffix
        return output
        