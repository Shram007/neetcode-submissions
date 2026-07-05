class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
        
        m, n = len(image), len(image[0])

        q = deque([(sr, sc)])
        image[sr][sc] = color
        dirs = [(1,0), (-1,0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr in range(m) and nc in range(n) and image[nr][nc] == orig):
                    image[nr][nc] = color
                    q.append((nr, nc))
        return image