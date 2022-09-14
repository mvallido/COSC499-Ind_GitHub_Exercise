def numberOfIslands(graph) -> int: 
    row, col = len(graph), len(graph[0])
    visited = set()
    count = 0
    
    def dfs(r,c):
        if r not in range(row) or c not in range(col) or graph[r][c] == "0" or (r,c) in visited:
            return
        
        visited.add((r,c))
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    
    for r in range(row):
        for c in range(col):
            if (r,c) not in visited and graph[r][c] == "1":
                dfs(r,c)
                count += 1
    
    return count
