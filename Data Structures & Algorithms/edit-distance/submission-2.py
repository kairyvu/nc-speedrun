class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # i: for word1
        # j: for word2
        
        # minDistance(i, j) = 1 + minDistance(i + 1, j)
        #                     minDistance(i + 1, j + 1) # if word1[i] == word2[j]
        #                     1 + minDistance(i + 1, j + 1)
        
        # return 

        m, n = len(word1), len(word2)
        memo = {}

        def calMinDistance(i, j):
            if i == m and j == n:
                return 0
            if i == m:
                return n - j # adding
            if j == n:
                return m - i # deleting
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                res = calMinDistance(i + 1, j + 1)
            else:
                delete = 1 + calMinDistance(i + 1, j)
                update = 1 + calMinDistance(i + 1, j + 1)
                insert = 1 + calMinDistance(i, j + 1)
                res = min(delete, update, insert)
            memo[(i, j)] = res
            return res
        
        return calMinDistance(0, 0)







