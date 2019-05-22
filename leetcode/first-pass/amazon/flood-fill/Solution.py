class Solution:
    def floodFill(self, image, sr, sc, newColor):
        n, m = len(image), len(image[0])
        color = image[sr][sc]
        stack = [(sr, sc)]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            x, y = node
            for (i, j) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < n and 0 <= j < m and image[i][j] == color:
                    stack.append((i, j))
        for x, y in visited:
            image[x][y] = newColor
        return image


