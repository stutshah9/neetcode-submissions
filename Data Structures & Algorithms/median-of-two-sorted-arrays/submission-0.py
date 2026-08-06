class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # run binairy search on A always which is the smaller array
        if len(B) < len(A):
            A, B = B, A

        left = 0
        right = len(A)-1

        while True:
            pointerA = (left + right) // 2 # pointer for A
            # pointerA and pointerB start at 0 that is why need to -2
            pointerB = half - pointerA - 2  # pointer for B
            
            Aleft = A[pointerA] if pointerA >= 0 else float("-infinity")
            Aright = A[pointerA + 1] if (pointerA + 1) < len(A) else float("infinity")
            Bleft = B[pointerB] if pointerB >= 0 else float("-infinity")
            Bright = B[pointerB + 1] if (pointerB + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft)+min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = pointerA - 1
            else:
                left = pointerA + 1

