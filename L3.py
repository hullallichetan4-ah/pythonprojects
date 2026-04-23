from collections import defaultdict

class Solution:
    def distance(self, nums):
        mp = defaultdict(list)

        # group indices
        for i, num in enumerate(nums):
            mp[num].append(i)

        n = len(nums)
        ans = [0] * n

        for lst in mp.values():
            size = len(lst)

            # prefix sum
            prefix = [0] * size
            prefix[0] = lst[0]
            for i in range(1, size):
                prefix[i] = prefix[i - 1] + lst[i]

            for i in range(size):
                idx = lst[i]

                sum_left = prefix[i - 1] if i > 0 else 0
                sum_right = prefix[-1] - prefix[i]

                count_left = i
                count_right = size - i - 1

                left = idx * count_left - sum_left
                right = sum_right - idx * count_right

                ans[idx] = left + right

        return ans
        
print(Solution().distance([1, 3, 1, 1, 2]))  # Output: [5, 0, 3, 4, 0]  
print(Solution().distance([0, 5, 3]))  # Output: [0, 0, 0]  
print(Solution().distance([1, 1, 1, 1, 1]))  # Output: [0, 0, 0, 0, 0]