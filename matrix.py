import numpy as np

def matexp(m, n):
    ret = m
    for i in range(n):
        ret = matmult(ret, m)
    return ret

def submat(m, rows, cols):
    new_matrix = []
    for row in rows:
        current_row = []
        for col in cols:
            current_row.append(m[row][col])
        new_matrix.append(current_row)
    return new_matrix

def rand_mat():
    return np.random.randn(2,2)

def matmult(a, b):
    return np.array(a).dot(np.array(b))

#https://stackoverflow.com/questions/10508021/matrix-multiplication-in-python
def matmult2(X, Y):
    if len(X[0]) != len(Y):
        print "Cannot multiply the two matrices. Incorrect dimensions."
        return
    result = [[0 for row in range(len(Y[0]))] for col in range(len(X))]
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

def matmult3(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 : 
    # zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]
