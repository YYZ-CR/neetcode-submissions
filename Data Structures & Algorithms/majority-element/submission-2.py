class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = dict()
        l = len(nums)//2 + 1
        for i in nums:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
            if c[i] >= l:
                    return i