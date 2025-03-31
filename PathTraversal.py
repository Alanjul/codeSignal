def path_traversal(grid, start_row, start_col):
    rows = len(grid)
    cols = len(grid[0])
    #check for valid input
    if (start_row < 0 or start_row >= rows or start_col < 0 or start_col >= 0):
        return "invalid input"
    directions = [(-1, 0),  #up
                  (1,0), #down
                  (0,1), #righ
                  (0,-1) #left
                  ]
    #start with the visited cells
    visited = [grid[start_row][start_col]]
    while True:
        #initialize maximum
        current_max = -1
        next_row = -1
        next_col = -1
        new_row = start_row + dir[0]
        new_col = start_col + dir[1]
        #checking if the new row and new_cols are out of bounds
        if new_row < 0 or new_row >= rows or new_col < 0 or new_col > cols:
            continue
        #checking if we have encountered a larger number in the cell
        if grid[new_row][new_col] > current_max:
            next_row, next_col, current_max = new_row, new_col, grid[new_row][new_col]
        #if we reach invalid cell break
        if current_max <= grid[start_row][start_col]:
            break
        #move to the next row
        start_row, start_col = next_row, next_col
        #append to max to visited
        visited.append(current_max)
    return visited



