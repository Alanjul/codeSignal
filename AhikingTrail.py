def find_next_uphill(grid, position):
    rows, cols = len(grid), len(grid[0])
    row, col = position
    if row <0 or row >= rows or col < 0 or col >= cols:
        return None
    directions = [(-1,0), (1,0),(0,-1),(0,1),
                 #diagnonal directions
                 (-1,1),(1,-1),(1,1),(-1,-1)]
    #next row
    next_row = grid[row][col]
    next_position = None
    for dr, dc in directions:
        new_row = row + dr
        new_col =  col + dc
        if (0<= new_row < rows) or (0 <= new_col < cols):
            if( grid[new_row][new_col] > next_row):
                next_row = grid[new_row][new_col]
                next_position = (new_row, new_col)
    return next_row if next_row != grid[row][col] else None

matrix = [[1,2,3],
          [6,5,8],
          [7,4,9]]
start_position = (1,1)
answer=find_next_uphill(matrix ,start_position)
print(answer)