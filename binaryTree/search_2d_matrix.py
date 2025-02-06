def SearchMatrix(target, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        if target == matrix[i][-1]: 
            return True
        elif target < matrix[i][-1]: 
            left, right = 0, cols - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False 
            
    return False
    
    


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(SearchMatrix(target, matrix))