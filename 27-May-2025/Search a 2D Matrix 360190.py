# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])


        start, end = 0, row - 1
        while start <= end:
            mid = (start + end) // 2
            if target > matrix[mid][-1]:
                start = mid + 1
            elif target < matrix[mid][0]:
                end = mid - 1
            else:
                break

        if not (start <= end):
            return False

        mid = (start + end) // 2
        l, r = 0, col - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[mid][m]:
                r = m - 1
            elif target > matrix[mid][m]:
                l = m + 1
            else:
                return True
        return False