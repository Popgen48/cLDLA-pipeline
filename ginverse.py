from scipy import linalg
import numpy
import sys

matrix = numpy.empty((0, 0))

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        row, col, value = map(float, line.split())  # Parse row, col, and value
        row -= 1
        col -= 1
        max_row = int(row) + 1
        max_col = int(col) + 1
        
        if max_row > matrix.shape[0]:
            matrix = numpy.pad(matrix, ((0, max_row - matrix.shape[0]), (0, 0)), mode='constant')
        if max_col > matrix.shape[1]:
            matrix = numpy.pad(matrix, ((0, 0), (0, max_col - matrix.shape[1])), mode='constant')
        
        matrix[int(row), int(col)] = value   

# Matrix is symmetrical
for i in range(matrix.shape[0]):
    for j in range(i+1, matrix.shape[1]):
        matrix[i][j] = matrix[j][i]
        
inverse = linalg.pinv(matrix)

with open(sys.argv[2], 'w') as output_file:
    for i in range(inverse.shape[0]):
        for j in range(i+1):
            output_file.write(f'{i+1}\t{j+1}\t{inverse[i][j]}\n')
            

