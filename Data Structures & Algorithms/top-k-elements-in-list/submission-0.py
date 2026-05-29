class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        most_freq = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                most_freq.append(num)
                if len(most_freq) == k:
                    return most_freq



        for i in range(len(nums)):
            if nums[i] in freq:
                index_i = freq.index(nums[i])
                freq[index_i].remove(nums[i])
                try:
                    freq[index_i+1].append(nums[i])
                except:
                    freq[index_i+1] = [nums[i]]
            else:
                try:
                    freq[1].append(nums[i])
                except:
                    freq[1] = [nums[i]]
        return 

