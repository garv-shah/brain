input_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]


def list_spiral_matrix(matrix, startWidth, endWidth, startHeight, endHeight):
    for i in range(startWidth, endWidth):
        print(matrix[0][i], end=" ")

    for i in range(startHeight + 1, endHeight - 1):
        print(matrix[i][endWidth - 1], end=" ")

    for i in range(startWidth, endWidth):
        # [::-1] reverses the array
        print(matrix[endHeight - 1][::-1][i], end=" ")

    for i in range(startHeight + 1, endHeight - 1):
        print(matrix[::-1][i][0], end=" ")

    if startWidth < endWidth and startHeight < endHeight:
        list_spiral_matrix(input_matrix, startWidth + 1, endWidth - 1, startHeight + 1, endHeight - 1)


list_spiral_matrix(input_matrix, 0, 4, 0, 4)
