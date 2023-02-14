"""

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        """
           L     R
         T 1,2,3
           4,5,6
           7,8,9
         B      

        update boundries after each layer top + 1, bottom  - 1



        """
        left, right = 0 , len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -=1

            if not (left < right and top < bottom):
                break

            for i in range( right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1


            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left +=1


        return res