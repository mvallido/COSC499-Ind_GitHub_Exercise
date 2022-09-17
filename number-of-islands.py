# Inline comment for video

def islandArea(graph) -> int:
    row, col = len(graph), len(graph[0])
    visited = set()
    largestIsland = 0
    
    def dfs(r,c):
        if r not in range(row) or c not in range(col) or graph[r][c] == 0 or (r,c) in visited:
            return 0
        
        visited.add((r,c))
        return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

    
    for r in range(row):
        for c in range(col):
            if (r,c) not in visited and graph[r][c] == 1:
                largestIsland = max(largestIsland, dfs(r,c))
    
    return largestIsland

def numberOfIslands(graph) -> int: 
    row, col = len(graph), len(graph[0])
    visited = set()
    count = 0
    
    def dfs(r,c):
        if r not in range(row) or c not in range(col) or graph[r][c] == 0 or (r,c) in visited:
            return
        
        visited.add((r,c))
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    
    for r in range(row):
        for c in range(col):
            if (r,c) not in visited and graph[r][c] == 1:
                dfs(r,c)
                count += 1
    
    return count

def init(graph) -> str:
    print(f"""
          Tested Graph:
          {graph}
          """)
    islandCount = numberOfIslands(graph)
    largestIsland = islandArea(graph)
    
    print(f"""
          The total number of islands in the graph above is {islandCount}
          Largest island in the graph above has an area of {largestIsland}
          """)

testCase1 = [[0, 1, 0, 1],
             [1, 1, 1, 1],
             [0, 1, 0, 1]]
testCase2 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0],
             [0,1,0,1,0,0,0,1,1,0,0,0,1]]

init(testCase1)
init(testCase2)