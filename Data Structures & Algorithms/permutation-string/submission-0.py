class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length1, length2 = len(s1), len(s2)
        if length1 > length2:
            return False
        
        count1, count2 = [0] * 26, [0] * 26
        for i in range(length1):
            count1[ord(s1[i]) - ord("a")] += 1
            count2[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        
        for i in range(length1, length2):
            if matches == 26:
                return True
            currIndex = ord(s2[i]) - ord("a")
            count2[currIndex] += 1
            if count1[currIndex] == count2[currIndex]:
                matches += 1
            elif count1[currIndex] == count2[currIndex] - 1:
                matches -= 1

            currIndex = ord(s2[i - length1]) - ord("a")
            count2[currIndex] -= 1
            if count1[currIndex] == count2[currIndex]:
                matches += 1
            elif count1[currIndex] == count2[currIndex] + 1:
                matches -= 1
        
        return matches == 26