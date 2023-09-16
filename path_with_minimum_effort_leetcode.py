class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        # The idea is to do binary search 
        def dfs(left, right, mid, visited):
            directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
            # This is base condition of getting out of the loop
            # When we start with (0,0) start and get to the end of the matrix that is: (rows=1, cols-1)
            # That means there is a path that exists which travels from top to bottom
            # Also the path has diff (which is difference between the adjacent cells less than the given mid)
            if left == rows-1 and right == cols-1:
                return True
            visited.add((left, right))
            for left_dir, right_dir in directions:
                new_left = left + left_dir
                new_right = right + right_dir
                if new_left >= 0 and new_left < rows and new_right >=0 and new_right < cols and (new_left, new_right) not in visited:
                    # This is difference of two points in the matrix
                    diff = abs(heights[left][right] - heights[new_left][new_right])
                    # This is a recursive call of the dfs function
                    if diff <= mid and dfs(new_left, new_right, mid, visited):
                        return True
            return False
                    

        # Calculating rows and columns
        rows = len(heights)
        cols = len(heights[0])

        # Initiating left and right for binary search
        left = 0
        right = 1000000

        while left<right:
            mid = (left+right)//2
            visited = set()
            if dfs(0, 0, mid, visited):
                right = mid
            else:
                left = mid+1
        return left




