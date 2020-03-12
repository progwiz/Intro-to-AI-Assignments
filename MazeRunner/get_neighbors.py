
#changing the order of the neighbors will change the efficiency of the dfs algorithm in particular.

def traversable_neighbors(dfs_maze, node):

    i,j = node
    neighbors = []

    if j+1 < len(dfs_maze):
        right = (i,j+1)
        if not(dfs_maze[right]):
            neighbors.append(right)

    if i+1 < len(dfs_maze):
        bottom = (i+1,j)
        if not(dfs_maze[bottom]):
            neighbors.append(bottom)

    if j-1 >= 0:
        left = (i,j-1)
        if not(dfs_maze[left]):
            neighbors.append(left)

    if i-1 >= 0:
        up = (i-1,j)
        if not(dfs_maze[up]):
            neighbors.append(up)

    return neighbors
