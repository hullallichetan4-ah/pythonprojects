#2078.TWo Furthest houses With Different Colors
#translated using AI
class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        maxDist = 0

        # Compare with first house
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                maxDist = i
                break

        # Compare with last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                maxDist = max(maxDist, n - 1 - i)
                break

        return maxDist

solution = Solution()
print(solution.maxDistance(["1","1","1","6","1","1","1"]))
print(solution.maxDistance(["1","8","3","8","3"]) )
print(solution.maxDistance(["0","1"]))