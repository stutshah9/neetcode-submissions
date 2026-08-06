class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1P = m-1
        num2P = n-1

        index = m+n-1

        while num1P >= 0 and num2P >= 0:
            if nums1[num1P] > nums2[num2P]:
                nums1[index] = nums1[num1P]
                num1P -= 1
            else:
                nums1[index] = nums2[num2P]
                num2P -= 1
            index -= 1
        
        if num2P >= 0:
            nums1[:index+1] = nums2[:num2P+1] 
