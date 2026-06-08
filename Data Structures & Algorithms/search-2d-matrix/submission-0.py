class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row = len(matrix)-1
        bot_row = 0
        target_row = -1
        top = len(matrix[0])-1
        bot = 0
        while top_row >= bot_row:
            mid_row = (top_row+bot_row)//2
            if matrix[mid_row][0] == target:
                return True
            elif matrix[mid_row][0] <= target <= matrix[mid_row][-1]: #if the target could be in that row
                target_row = mid_row
                break
            elif matrix[mid_row][0] > target:
                top_row = mid_row-1
            elif matrix[mid_row][0] < target:
                bot_row = mid_row+1
        if target_row == -1:
            return False
        while top >= bot:
            mid = (top+bot)//2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                top = mid-1
            elif matrix[target_row][mid] < target:
                bot = mid+1
        return False

            