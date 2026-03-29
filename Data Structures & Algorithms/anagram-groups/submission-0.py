class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sortStr = ''.join(sorted(s))
            anagrams[sortStr].append(s)
        
        return [lst for lst in anagrams.values()]