class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, prevHeight, visited):
            if (r, c) in visited or not 0 <= r < rows or not 0 <= c < cols or heights[r][c] < prevHeight:
                return
            visited.add((r, c))
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)

        for i in range(rows):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, cols - 1, heights[i][cols - 1], atl)
        
        for i in range(cols):
            dfs(0, i, heights[0][i], pac)
            dfs(rows - 1, i, heights[rows - 1][i], atl)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
    
        return res