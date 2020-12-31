# Calculation with Matrices
> Python class that facilitates matrix calculations.

## Installation

> from matrix import Matrix
<p>Download the matrix.py file and place it in your project folder. Then, import the class Matrix into your program.</p>

## Instantiation

> matrix = Matrix(n_rows, n_columns, matrix_list)

- _n_rows standart value: 1._
- _n_columns standart value: 1._
- _matrix_list standart value: 'random'._
- _Leave 'random' in matrix_list to apply random values to the matrix. If not, insert a list to generate a matrix object with its values._

## Functions

- **Addition:**
    - > matrix_A + Matrix_B ... or ... matrix_A += Matrix_B 

- **Subtraction:**
    - > matrix_A - Matrix_B ... or ... matrix_A -= Matrix_B 
    
- **Multiplication:**
    - > matrix_A * Matrix_B ... or ... matrix_A *= Matrix_B 
    
- **Transposition:**
    - > matrix_A = matrix_A.transpose()
    
- **Hadamart product:**
    - > Matrix.hadamart(matrix_A, matrix_B) 
    
- **Sigmoid function:**
    - > matrix_A = matrix_A.sigmoid() 
    
- **Derived from the sigmoid function:**
    - > matrix_A = matrix_A.derivative_sigmoid()
    
**note: The hadamart function is a statistical method to stay on the standard: 'matrix_A' 'operation' 'matrix _B'.

To learn how to do matrix calculations, [click here.](https://www.theinformationlab.co.uk/2017/05/26/introduction-matrix-calculations/)
