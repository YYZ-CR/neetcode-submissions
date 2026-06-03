class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_queue = [] #holds indices of the queue of max values
        max_list = []
        for i in range(len(nums)):
            while max_queue and nums[max_queue[-1]] < nums[i]:
                max_queue.pop(-1)
            max_queue.append(i)
            if i >= k-1: # when i reaches the end of the first window
                max_list.append(nums[max_queue[0]])
                if i-k+1 == max_queue[0]:
                    max_queue.pop(0)
        return max_list
                