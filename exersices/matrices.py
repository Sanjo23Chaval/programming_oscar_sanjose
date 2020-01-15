def fill_matrix(matrix1,matrix2):
    q = 0
    matrix_res = []
    for i in range(len(matrix1)):
        matrix_res.append([])
        for z in range(len(matrix1[i])):
            matrix_res[i].append(0)
            while q < len(matrix1):
                matrix_res[i][z] += matrix1[i][q] * matrix2[q][z]
                q += 1
            q = 0
    return matrix_res

def print_cool_matrix(matrix_res):
    for i in range(len(matrix_res)):
        for z in range(len(matrix_res[i])):
            matrix_res[i][z] = str(matrix_res[i][z])
        print "\t".join(matrix_res[i])

A = [[2,4],
    [3,1]]
B = [[2,1],
     [1,3]]

C = fill_matrix(A,B)
print_cool_matrix(C)
