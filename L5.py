from collections import deque

class Solution:
    def hasValidPath(self, grid):
        if not grid or not grid[0]:
            return False
        m, n = len(grid), len(grid[0])
        
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        
        while q:
            r, c = q.popleft()
            
            if (r, c) == (m - 1, n - 1):
                return True
            
            for dx, dy in dirs[grid[r][c]]:
                nr, nc = r + dx, c + dy
                
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    
                    # check reverse connection
                    for bdx, bdy in dirs[grid[nr][nc]]:
                        if nr + bdx == r and nc + bdy == c:
                            visited.add((nr, nc))
                            q.append((nr, nc))
                            break
        
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.hasValidPath([[2,4,3],[6,5,2]]))
    print(sol.hasValidPath([[1,2,1],[1,2,1]]))
    print(sol.hasValidPath([[1,1,2]]))  