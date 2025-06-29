import numpy as np

# Function: Add two matrices
def add_matrix(A, B):
    return np.array(A) + np.array(B)

# Function: Subtract matrix B from matrix A
def sub_matrix(A, B):
    return np.array(A) - np.array(B)

# Function: Multiply two matrices (dot product)
def multi_matrix(A, B):
    return np.dot(np.array(A), np.array(B))

# Function: Transpose a matrix
def transpose_matrix(A):
    return np.array(A).T

# Function: Compute the determinant of a matrix
def deter_matrix(A):
    return np.linalg.det(np.array(A))

# Function: Compute the inverse of a matrix (if invertible)
def inverse_matrix(A):
    try:
        return np.linalg.inv(np.array(A))  # Attempt to compute inverse
    except np.linalg.LinAlgError:
        print("Matrix is not invertible (singular matrix).")
        return None  # Return None if not invertible

# Function: Matrix calculator CLI
def matrix_cli():
    # Step 1: Get matrix dimensions from the user
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    A, B = [], []  # Initialize matrices A and B as empty lists

    # Step 2: Get values for Matrix A
    print("Enter values for matrix A:")
    for i in range(rows):
        row = [float(input(f"Enter A[{i}][{j}]: ")) for j in range(cols)]
        A.append(row)

    # Step 3: Get values for Matrix B
    print("Enter values for matrix B:")
    for i in range(rows):
        row = [float(input(f"Enter B[{i}][{j}]: ")) for j in range(cols)]
        B.append(row)

    # Step 4: Display the input matrices
    print("\nMatrix A:\n", np.array(A))
    print("Matrix B:\n", np.array(B))
    print("-" * 70)

    # Step 5: Perform and display results of basic matrix operations
    print("A + B:\n", add_matrix(A, B))
    print("A - B:\n", sub_matrix(A, B))
    print("A * B:\n", multi_matrix(A, B))

    print("-" * 70)

    # Step 6: Display transposed matrices
    print("Transpose of A:\n", transpose_matrix(A))
    print("Transpose of B:\n", transpose_matrix(B))

    # Step 7: Only compute determinant and inverse if the matrices are square
    if rows == cols:
        print("-" * 70)
        print("Determinant of A:", round(deter_matrix(A), 2))
        print("Determinant of B:", round(deter_matrix(B), 2))

        print("-" * 70)
        invA = inverse_matrix(A)
        invB = inverse_matrix(B)

        # Step 8: Display inverses if they exist
        if invA is not None:
            print("Inverse of A:\n", np.round(invA, 2))
        if invB is not None:
            print("Inverse of B:\n", np.round(invB, 2))
    else:
        print("-" * 70)
        print("Skipping inverse and determinant: matrices are not square.")

# Run the matrix calculator
matrix_cli()
