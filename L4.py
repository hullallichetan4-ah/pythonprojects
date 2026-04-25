import bisect 
class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        nums = []
        
        def convert(x,y):
            if y==0:
                return x
            elif x == side:
                return y + side
            elif y == side:
                return 3*side - x 
            elif x == 0:
                return 4*side - y
            
        for [x,y] in points:
            nums.append(convert(x,y))
            
        nums.sort()
        for i in range(len(nums)):
            nums.append(4*side+nums[i])
        
        def judge(target):
            if target > side:
                return False
            
            loc = bisect.bisect_left(nums,nums[0]+target)
            
            if loc >= len(nums)//2:
                return False
            
            for i in range(loc):
                flag = True
                curr = i
                for _ in range(k-1):
                    l = bisect.bisect_left(nums,nums[curr]+target)
                    if l >= i + len(nums)//2:
                        flag = False
                        break
                    curr = l
                
                if flag and nums[i+len(nums)//2] - nums[curr] >= target:
                    return True
                
            return False

        front = 1
        rear = side + 1
        while front < rear:
            mid = (front + rear)//2
            
            if judge(mid):
                front = mid + 1
            else:
                rear = mid 
                
        return front - 1
    print(maxDistance(5,2,[[0,2],[2,0],[2,2],[0,0]],2))  # Output: 2
    print(maxDistance(5,2,[[0,0],[1,2],[2,0],[2,2],[2,1]],4))  # Output: 1
    print(maxDistance(5,2,[[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]],5))  # Output: 1