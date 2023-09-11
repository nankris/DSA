def numIslands(grid):
    def dfs_visited(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return
        # Marking the visited 1 as 0 so that we don't count this again
        if grid[i][j] == "1":
            grid[i][j] = "0"
        dfs_visited(grid, i+1,j) # visit down
        dfs_visited(grid, i-1,j) # visit up
        dfs_visited(grid, i,j+1) # visit right
        dfs_visited(grid, i,j-1) # visit left

    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                islands += 1
                dfs_visited(grid, i, j)
    return islands        
    

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))

