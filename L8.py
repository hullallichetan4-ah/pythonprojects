class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = nums1 + nums2
        # Sort the merged array
        l = sorted(l1)
        # Get length
        leng = len(l)
        # If odd length, return middle element
        if leng % 2 != 0:
            ans = (leng // 2)
            return l[ans] 
        # If even length, return average of two middle elements
        elif leng % 2 == 0:
            ans = (l[leng // 2] + l[(leng // 2) - 1]) / 2.0
            return ans 
        
sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
print(sol.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
print(sol.findMedianSortedArrays([0, 0], [0, 0]))  # Output: 0.0