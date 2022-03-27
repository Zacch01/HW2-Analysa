# Matrix Solver in Gaussian Elimination and LU Decomposition.

MATRIX_COUNT = 0


def multiplyMatrix(matrixA, matrixB, isTrue):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrixA: NxM Matrix
    :param matrixB: NxM Matrix
    :param isTrue: boolean which decide if save matrices in a list
    :return: NxM matrix
    """
    # Initialize NxM matrix filled with zeros
    matrixC = [[0.0] * len(matrixB[0]) for _ in range(len(matrixA))]

    # Multiply the two matrices and store the outcome in matrixC
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

    # Saving the matrices in the right lists
    if isTrue:
        global MATRIX_COUNT
        with open("GaussianElimination.txt", 'a+') as f:
            f.write('=================================================================================================')

            f.write('\nElementary Matrix [' + str(MATRIX_COUNT) + ']\n')
            for i in range(len(matrixA)):
                for j in range(len(matrixA)):
                    temp = '{: ^22}'.format(matrixA[i][j])
                    f.write(temp)
                f.write('\n')

            f.write('\npreMultiply Matrix [' + str(MATRIX_COUNT) + ']\n')
            for i in range(len(matrixB)):
                for j in range(len(matrixB)):
                    temp = '{: ^22}'.format(matrixB[i][j])
                    f.write(temp)
                f.write('\n')

            f.write('\nafterMultiply Matrix [' + str(MATRIX_COUNT) + ']\n')
            for i in range(len(matrixC)):
                for j in range(len(matrixC)):
                    temp = '{: ^22}'.format(matrixC[i][j])
                    f.write(temp)
                f.write('\n')

        MATRIX_COUNT = MATRIX_COUNT + 1

    # Return the outcome matrix
    return matrixC


