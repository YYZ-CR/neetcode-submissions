class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 in s:
                continue
            count = 0
            while nums[i]+count in s:
                count += 1
            longest = max(count, longest)
        return longest


        