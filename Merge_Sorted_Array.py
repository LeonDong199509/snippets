class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # Original solution
        l = len(nums1)
        i = 0
        j = 0
        last_sorted = -1
        while (i < m and j < n):
            if nums1[i] <= nums2[j]:
                i += 1
                last_sorted += 1
            else:
                # Move the remaining index to right
                for i_i in range(l-1-i, 0, -1):
                    nums1[i+i_i] = nums1[i+i_i-1]
                nums1[i] = nums2[j]
                j += 1
                i += 1
                m += 1
                last_sorted += 1

        # Add remaining values in nums2 to nums1
        if j < n:
            while (j < n):
                nums1[last_sorted+1] = nums2[j]
                last_sorted += 1
                j += 1

    def merge_optimized(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Optimized solution
        # Ideas: If we start from the end, we don't need to move the remaining elements in nums1

        i = m - 1
        j = n - 1
        c = m + n - 1

        if j >= 0:
        
            while (i >= 0 or j >= 0):
                if i >= 0 and j >= 0 and nums1[i] >= nums2[j]:
                    nums1[c] = nums1[i]
                    i -= 1
                elif i >= 0 and j >= 0 and nums1[i] < nums2[j]:
                    nums1[c] = nums2[j]
                    j -= 1
                elif i >= 0 and j < 0:
                    i -= 1
                elif i < 0 and j >= 0:
                    nums1[c] = nums2[j]
                    j -= 1
                c -= 1
