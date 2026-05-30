class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            for j in range(len(nums[i+1:])):
                try:
                    ind = nums[i+1+j+1:].index(-(nums[i] + nums[i+1+j]))
                    if [nums[i], nums[i+1+j], nums[i+1+j+1+ind]] in triplets:
                        continue
                    triplets.append([nums[i], nums[i+1+j], nums[i+1+j+1+ind]])
                except:
                    pass
        return triplets
                