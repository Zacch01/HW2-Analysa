def findInverse(matrix, vector):
    """
    Solve the matrix into an Identity matrix, updating the vector of the matrix, and return the inverse matrix of matrix
    :param matrix: NxN matrix
    :param vector: Nx1 vector solution of the matrix
    :return: Inverse NxN matrix, the inverse matrix of matrix
    """
    # Initialize inverseMatrix into an Identity matrix
    inverseMatrix = [[1.0 if row == col else 0.0 for col in range(len(matrix))] for row in range(len(matrix))]

    # Solving matrix into an Upper matrix
    for i in range(len(matrix)):
        # Calling function to reArrange the matrix, and the vector
        matrix, vector = checkPivotColumn(matrix, vector, i)

        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:
                # Multiply into an Upper matrix, updating matrix vector as well, and keep the inverseMatrix updated
                vector = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), vector, False)
                inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), inverseMatrix, False)
                matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), matrix, True)

    # Solving matrix into a Lower matrix
    for i in reversed(range(len(matrix))):
        for j in reversed(range(i)):
            # Multiply into a Lower matrix, updating matrix vector as well, and keep the inverseMatrix updated
            if matrix[j][i] != 0:
                vector = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), vector, False)
                inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), inverseMatrix, False)
                matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), matrix, True)

    # Return the inverse matrix, and the updated solution vector of the matrix
    return inverseMatrix, vector


def checkPivotColumn(matrix, vector, index):
    """
    Taking care that the pivot in the column [index] will be the highest one, and return the updated matrix and vector
    :param matrix: NxN matrix
    :param vector: Nx1 vector solution of the matrix
    :param index: Column index
    :return: The updated matrix and vector
    """
    # Variable to store the max pivot in specific column
    maxPivot = abs(matrix[index][index])

    # Variable to store the new pivot row
    pivotRow = 0

    for j in range(index + 1, len(matrix)):
        # In case there's a higher pivot
        if abs(matrix[j][index]) > maxPivot:
            # Store the new highest pivot, and his row
            maxPivot = abs(matrix[j][index])
            pivotRow = j

    # In case there was a higher pivot, change between the matrix rows
    if maxPivot != abs(matrix[index][index]):
        # Initialize elementary matrix to swap the matrix rows
        elementaryMatrix = [[1.0 if x == y else 0.0 for y in range(len(matrix))] for x in range(len(matrix))]
        elementaryMatrix[index], elementaryMatrix[pivotRow] = elementaryMatrix[pivotRow], elementaryMatrix[index]

        # Changed the Matrix and the vector Rows
        matrix = multiplyMatrix(elementaryMatrix, matrix, True)
        vector = multiplyMatrix(elementaryMatrix, vector, False)

    # In case the pivot isn't one, we will make sure it will be one
    if matrix[index][index] != 1:
        vector = multiplyMatrix(initElementaryMatrix(len(matrix), index, index, 1 / matrix[index][index]), vector, False)
        matrix = multiplyMatrix(initElementaryMatrix(len(matrix), index, index, 1 / matrix[index][index]), matrix, True)

    # Return the updated matrix and vector
    return matrix, vector


def matrixCond(matrix, inverseMatrix):
    """
    Multiply the max norm of the origin and inverse matrix, and return its solution accuracy
    :param matrix: NxN matrix
    :param inverseMatrix: NxN inverse matrix of matrix
    :return: Matrix solution precision
    """
    return infinityNorm(matrix) * infinityNorm(inverseMatrix)
