def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    else:
        for i in range(0,len(matrix)):
            for j in range(0, len(matrix[i])):
                if j < len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j]))