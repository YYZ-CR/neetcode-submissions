class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        longest = 0
        for i in range(len(s)):
            if s[i] in s[start:i]:
                while s[i] in s[start:i]:
                    start += 1
                    if end < start: 
                        end = start
            else:
                end = i
                longest = max(longest, end - start + 1)
        return longest