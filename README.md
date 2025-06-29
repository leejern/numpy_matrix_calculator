# Matrix Calculator

A comprehensive Python-based matrix calculator that performs various matrix operations using NumPy. This interactive command-line tool allows users to input two matrices and perform multiple mathematical operations on them.

## Features

### Basic Matrix Operations
- **Addition**: Adds two matrices element-wise
- **Subtraction**: Subtracts matrix B from matrix A
- **Multiplication**: Computes matrix multiplication (dot product)
- **Transpose**: Returns the transpose of both matrices

### Advanced Operations (Square Matrices Only)
- **Determinant**: Calculates the determinant of square matrices
- **Inverse**: Computes the inverse of matrices (if they exist)

## Requirements

- Python 3.6 or higher
- NumPy library

## Installation

1. Make sure you have Python installed on your system
2. Install NumPy using pip:
```bash
pip install numpy
```

## Usage

1. Run the script:
```bash
python matrix_calculator.py
```

2. Follow the interactive prompts:
   - Enter the number of rows and columns for your matrices
   - Input values for Matrix A (row by row)
   - Input values for Matrix B (row by row)

3. The program will automatically display:
   - Both input matrices
   - Results of addition, subtraction, and multiplication
   - Transposed matrices
   - Determinant and inverse (for square matrices only)

## Example Run

```
Enter number of rows: 2
Enter number of columns: 2
Enter values for matrix A:
Enter A[0][0]: 1
Enter A[0][1]: 2
Enter A[1][0]: 3
Enter A[1][1]: 4
Enter values for matrix B:
Enter B[0][0]: 5
Enter B[0][1]: 6
Enter B[1][0]: 7
Enter B[1][1]: 8

Matrix A:
 [[1. 2.]
  [3. 4.]]
Matrix B:
 [[5. 6.]
  [7. 8.]]
----------------------------------------------------------------------
A + B:
 [[ 6.  8.]
  [10. 12.]]
A - B:
 [[-4. -4.]
  [-4. -4.]]
A * B:
 [[19. 22.]
  [43. 50.]]
----------------------------------------------------------------------
Transpose of A:
 [[1. 3.]
  [2. 4.]]
Transpose of B:
 [[5. 7.]
  [6. 8.]]
----------------------------------------------------------------------
Determinant of A: -2.0
Determinant of B: -2.0
----------------------------------------------------------------------
Inverse of A:
 [[-2.   1. ]
  [ 1.5 -0.5]]
Inverse of B:
 [[-4.   3. ]
  [ 3.5 -2.5]]
```

## Function Reference

### Core Functions

- `add_matrix(A, B)`: Returns the sum of matrices A and B
- `sub_matrix(A, B)`: Returns A - B
- `multi_matrix(A, B)`: Returns the matrix product A × B
- `transpose_matrix(A)`: Returns the transpose of matrix A
- `deter_matrix(A)`: Returns the determinant of square matrix A
- `inverse_matrix(A)`: Returns the inverse of matrix A (if it exists)

### Main Function

- `matrix_cli()`: Interactive command-line interface for the calculator

## Error Handling

- **Non-invertible matrices**: If a matrix is singular (determinant = 0), the program will display "Matrix is not invertible" and return None
- **Non-square matrices**: Determinant and inverse operations are automatically skipped for non-square matrices
- **Matrix dimension mismatch**: NumPy will handle dimension compatibility for operations

## Limitations

- Determinant and inverse calculations are only performed on square matrices
- Matrix multiplication requires compatible dimensions (columns of A = rows of B)
- All input values are converted to float for numerical precision

## File Structure

```
matrix_calculator.py    # Main script file
README.md              # This documentation file
```

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional matrix operations (eigenvalues, SVD, etc.)
- Better error handling and input validation
- GUI implementation
- Support for complex numbers
- Matrix file import/export functionality

## License

This project is open source and available under the MIT License.

## Author

Created as a educational tool for learning matrix operations and NumPy usage.# numpy_matrix_calculator
