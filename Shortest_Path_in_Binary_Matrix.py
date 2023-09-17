# Technique using breadth first search
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1        

        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue = [(0, 0, 1)]

        while queue:
            i, j, steps = queue.pop(0)
            if i == rows-1 and j == cols-1:
                return steps
            for di, dj in directions:
                x = i+di
                y=j+dj
                if x >= 0 and x < rows and y >= 0 and y < cols and grid[x][y] == 0:
                    queue.append((x, y, steps+1))
                    grid[x][y] = 1
        return -1
