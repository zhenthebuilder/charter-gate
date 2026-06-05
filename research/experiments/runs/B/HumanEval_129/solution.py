def minPath(grid, k):
    n = len(grid)
    
    # Find position of 1
    start_pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start_pos = (i, j)
                break
        if start_pos:
            break
    
    path = [1]
    pos = start_pos
    
    for _ in range(k - 1):
        i, j = pos
        neighbors = []
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                neighbors.append((grid[ni][nj], (ni, nj)))
        
        # Greedily pick the smallest neighbor
        val, next_pos = min(neighbors, key=lambda x: x[0])
        path.append(val)
        pos = next_pos
    
    return path
