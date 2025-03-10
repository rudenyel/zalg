from typing import List

def gauss_jordan_inverse(
        matrix: List[List[float]],
        threshold: float = 1e-10) -> List[List[float]]:
    # Gaussian elimination is a useful and easy way to compute the inverse of a matrix.
    # To compute a matrix inverse using this method, an augmented matrix is first created
    # with the left side being the matrix to invert and the right side being the identity matrix.
    # Then, Gaussian elimination is used to convert the left side into the identity matrix,
    # which causes the right side to become the inverse of the input matrix.

    n = len(matrix)

    # The first step to compute its inverse is to create the augmented matrix.
    # matrix = [
    #     [4, 7],
    #     [2, 6]
    # ]
    augmented = [row + [1.0 if i == j else 0.0 for j in range(n)]
                 for i, row in enumerate(matrix)]
    # augmented = [
    #     [4, 7, 1, 0],
    #     [2, 6, 0, 1]
    # ]

    for i in range(n):
        # Partial Pivoting:
        # Select the pivot element with the largest absolute value from the column.
        # Swap rows to move this element into the pivot position.
        # This improves numerical stability by reducing rounding errors.
        max_row = i
        for k in range(i, n):
            if abs(augmented[k][i]) > abs(augmented[max_row][i]):
                max_row = k
        # Swap rows
        augmented[i], augmented[max_row] = augmented[max_row], augmented[i]

        # Checking the matrix for regularity
        # Comparing matrix elements to zero in numerical calculations can be unreliable
        # due to rounding errors and the limited precision of floating point representation.
        # Instead, it is better to use a threshold value to determine
        # if an element can be considered “null”. This makes the algorithm more stable.
        if abs(augmented[i][i]) < threshold:
            raise ValueError("The matrix is not regular, the inverse matrix does not exist.")

        # i = 0
        # augmented = [
        #     [4, 7, 1, 0],
        #     [2, 6, 0, 1]
        # ]
        # i = 1
        # augmented = [
        #     [1, 1.75, 0.25, 0],
        #     [0, 2.5, -0.5, 1]
        # ]

        # Normalization of the leading line
        # (make the diagonal element equal to 1)
        divisor = augmented[i][i]
        for j in range(i, 2 * n):
            augmented[i][j] /= divisor
        # i = 0
        # augmented = [
        #     [1, 1.75, 0.25, 0],
        #     [2, 6, 0, 1]
        # ]
        # i = 1
        # augmented = [
        #     [1, 1.75, 0.25, 0],
        #     [0, 1, -0.2, 0.4]
        # ]

        # Zeroing elements above and below the diagonal
        for k in range(n):
            if k != i and augmented[k][i] != 0:
                factor = augmented[k][i]
                for j in range(i, 2 * n):
                    augmented[k][j] -= factor * augmented[i][j]
        # i = 0
        # augmented = [
        #     [1, 1.75, 0.25, 0],
        #     [0, 2.5, -0.5, 1]
        # ]
        # i = 1
        # augmented = [
        #     [1, 0, 0.6, -0.7],
        #     [0, 1, -0.2, 0.4]
        # ]

    # Extracting the inverse matrix from the right part
    inverse = [row[n:] for row in augmented]
    # inverse = [
    #     [0.6, -0.7],
    #     [-0.2, 0.4]
    # ]

    return inverse

def input_matrix() -> List[List[float]]:
    n = int(input("Enter the rank of the square matrix n: "))
    matrix = []
    print("Enter the matrix row by row (with space):")
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != n:
            raise ValueError("Incorrect number of elements in the row")
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    try:
        A = input_matrix()
        # A = [
        #    [4, 7],
        #    [2, 6]
        # ]
        inverted = gauss_jordan_inverse(A)
        # inverted = [
        #    [0.6, -0.7],
        #    [-0.2, 0.4]
        # ]
        print("Inverted matrix: ")
        for row in inverted:
            print([round(x, 3) for x in row])
    except ValueError as e:
        print(e)