from typing import List

class Solution:
    '''
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        # TODO: Implement
        return 0
        
        
solver = Solution()

# 1
inputGrid = [
    '11110',
    '11010',
    '11000',
    '00000',
]

# 3
# inputGrid = [
#     '11000',
#     '11000',
#     '00100',
#     '00011',
# ]

print(solver.numIslands(inputGrid))