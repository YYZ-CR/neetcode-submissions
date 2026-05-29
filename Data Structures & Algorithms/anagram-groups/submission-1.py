class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = dict()
        for i in strs:
            sortedi = ''.join(sorted(i))
            if sortedi not in words:
                words[sortedi] = []            
            words[sortedi].append(i)
        return list(words.values())