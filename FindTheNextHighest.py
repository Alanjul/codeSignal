"""Ready for a new challenge? Your task is to find the next higher peak
based on the hiker('s current position. Consider directions carefully as you '
'craft your solution. Remember, the peak must be higher than the hiker's
current elevation. Let's see"""
def findNextPeak(matrix, row, col):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    #initialize the current height
    current_height = matrix[row][col]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        # TODO: Check if the new position is within bounds and higher than the current
        if 0 <= r < rows and 0 <= c < cols and matrix[r][c] > current_height:
            return (r, c)  # Return coordinates of the next higher peak
    return (row, col)  # No higher peak, stay in place

    # Hiking exploration example where the hiker looks for a higher peak around
trail_map = [
        [3, 5, 6],
        [4, 7, 8],
        [1, 2, 9]
    ]
start_position = (1, 1)  # Starting at elevation 7
next_peak = findNextPeak(trail_map, start_position[0], start_position[1])
print("Next peak at coordinates:", next_peak)
