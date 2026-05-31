class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longest = 0
        for i in range(len(s)):
            if len(s[left:i+1])-s[left:i+1].count(max(set(s), key = s[left:i+1].count))>k:
                #length of the window - max appearance letter > # of things u can replace
                while len(s[left:i+1])-s[left:i+1].count(max(set(s), key = s[left:i+1].count))>k:
                    left += 1
            longest = max(longest, i-left+1)
        return longest