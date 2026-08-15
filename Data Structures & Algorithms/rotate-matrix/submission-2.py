class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # rotate starting with outer layer
        # move inwards
        # corner: top left -> top right -> bottom right -> bottom left
        
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while left < right:
            for i in range(right - left):
                # top left to top right
                temp = matrix[top + i][right]
                matrix[top + i][right] = matrix[top][left + i]

                # top right to bottom right
                temp1 = matrix[bottom][right - i]
                matrix[bottom][right - i] = temp

                # bottom right to bottom left
                temp2 = matrix[bottom - i][left]
                matrix[bottom - i][left] = temp1

                # bottom left to top left
                matrix[top][left + i] = temp2
            
            left += 1
            right -= 1
            bottom -= 1
            top += 1
        
