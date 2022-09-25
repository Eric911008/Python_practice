import numpy as np
input_matrix = np.array(
    [[16, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 5], [0, 0, 0, 0]])
print("The input matrix is:")
print(input_matrix)
sparse_matrix = []
rows, cols = input_matrix.shape
for i in range(rows):
    for j in range(cols):
        if input_matrix[i][j] != 0:
            triplet = [i, j, input_matrix[i][j]]
            sparse_matrix.append(triplet)
print("The sparse matrix is:")
print(sparse_matrix)
