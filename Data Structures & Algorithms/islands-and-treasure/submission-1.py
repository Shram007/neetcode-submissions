class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        q = deque()

        # add each treasure spot to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dist = 1 # start at dist 1 since 0 dist is a treasure spot
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                # for each adj spot, update islands and add them to queue
                for dr, dc in dirs:
                    if (r + dr in range(ROWS) and c + dc in range(COLS) 
                        and grid[r + dr][c + dc] == INF):
                        q.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = dist

            # increase dist at the end of bfs layer
            dist += 1

