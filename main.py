# Matrix Solver in Gaussian Elimination Method

# Global Variable [Only Used To print the iteration number]
MATRIX_COUNT = 0


def printIntoFile(data, message, isTrue):
    """
    Printing the data and the message content into a specified file
    :param data: Data from a user
    :param message: Message that contain the data subject
    :param isTrue: Boolean parameter, which help to navigate to the right section
    """
    # Our Global Variable To Count The Iteration Number
    global MATRIX_COUNT

    # In Case We Are Running A New Linear Equation, It will erase the lase one
    if MATRIX_COUNT == 0:
        file = open('GaussianElimination.txt', 'w')
        file.close()

    # Open the file and save the data
    with open('GaussianElimination.txt', 'a+') as file:
        # In case we are in an iteration solution
        if isTrue:
            # In case we are printing new calculation
            if MATRIX_COUNT % 3 == 0:
                file.write('==========================================================================================')

            # Saving the matrix in the file
            file.write('\n' + str(message) + ' [' + str(MATRIX_COUNT) + ']\n')
            for i in range(len(data)):
                for j in range(len(data[0])):
                    objectData = '{: ^22}'.format(data[i][j])
                    file.write(objectData)
                file.write('\n')

            # Increase Our Global Iteration Counter Variable
            MATRIX_COUNT = MATRIX_COUNT + 1

        # Our Solution Data
        else:
            # In case we are printing the solution accuracy
            file.write('==============================================================================================')
            file.write('\n[' + str(message) + ']\n')
            file.write(str(data))
            file.write('\n')


def gaussianElimination():
    """
    Solving linear equation in Gaussian Elimination method
    """
    # Initialize the matrix, and vectorB
    originMatrix, vectorB = initMatrix()

    # Check if the matrix is Quadratic matrix, and check if vectorB is in appropriate size
    if len(originMatrix) == len(originMatrix[0]) and (len(vectorB) == 1 and len(vectorB[0]) == len(originMatrix)):

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            # Getting the inverse matrix of originMatrix, and the fixed vectorB
            inverseMatrix, vectorB = findInverse(originMatrix, vectorB)

            # Getting the accuracy of the solution
            solutionPrecision = matrixCond(originMatrix, inverseMatrix)

            # Saving the matrix solution
            printIntoFile(vectorB, 'Matrix Solution', True)
            printIntoFile(solutionPrecision, 'Solution Accuracy Rate', False)

        # According message In case there is more or less than one solution
        else:
            print('This Is A Singular Matrix')

    # In case the input Linear Equation isn't meet the demands
    else:
        print("The Input Linear Equation Isn't Match")
