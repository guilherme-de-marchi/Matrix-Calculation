# My Github: https://github.com/Guilherme-De-Marchi

from random import random
from math import e as eulers_number

class Matrix:
    def __init__(self, n_rows=0, n_columns=0, matrix_list='random'):
        ''' Configurations: random -> random values ​​for the matrix
            or insert a list to use it.'''
        
        if matrix_list == 'random':
            self.matrix = [[random() for column in range(n_columns)] for row in range(n_rows)]

        elif type(matrix_list) == list:
            self.matrix = matrix_list

        else:
            raise ValueError('Matrix "matrix_list" argument incorrect.')

    def __str__(self):
        return f'{self.matrix}'

    def __add__(self, other):
        if type(other) is not Matrix:
            raise TypeError('It is not possible to add a matrix to an object that is not a matrix.')

        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]): 
            raise ValueError('It is not possible to add matrices with different sizes.')

        result = Matrix(matrix_list=[])

        for index_row in range(len(self.matrix)):
            result.matrix.append([])

            for index_column in range(len(self.matrix[index_row])):
                result.matrix[-1].append(self.matrix[index_row][index_column] + other.matrix[index_row][index_column])

        return result

    def __iadd__(self, other):
        if type(other) is not Matrix:
            raise TypeError('It is not possible to add a matrix to an object that is not a matrix.')

        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]): 
            raise ValueError('It is not possible to add matrices with different sizes.')

        result = Matrix(matrix_list=[])

        for index_row in range(len(self.matrix)):
            result.matrix.append([])

            for index_column in range(len(self.matrix[index_row])):
                result.matrix[-1].append(self.matrix[index_row][index_column] + other.matrix[index_row][index_column])

        return result

    def __sub__(self, other):
        if type(other) is not Matrix:
            raise TypeError('It is not possible to subtract a matrix to an object that is not a matrix.')

        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]): 
            raise ValueError('It is not possible to subtract matrices with different sizes.')

        result = Matrix(matrix_list=[])

        for index_row in range(len(self.matrix)):
            result.matrix.append([])

            for index_column in range(len(self.matrix[index_row])):
                result.matrix[-1].append(self.matrix[index_row][index_column] - other.matrix[index_row][index_column])

        return result

    def __isub__(self, other):
        if type(other) is not Matrix:
            raise TypeError('It is not possible to subtract a matrix to an object that is not a matrix.')

        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]): 
            raise ValueError('It is not possible to subtract matrices with different sizes.')

        result = Matrix(matrix_list=[])

        for index_row in range(len(self.matrix)):
            result.matrix.append([])

            for index_column in range(len(self.matrix[index_row])):
                result.matrix[-1].append(self.matrix[index_row][index_column] - other.matrix[index_row][index_column])

        return result

    def __mul__(self, other):
        if type(other) is not Matrix:
            raise TypeError('It is not possible to multiply a matrix with an object that is not a matrix.')

        if len(self.matrix) != len(other.matrix[0]) and len(other.matrix) != len(self.matrix[0]): 
            raise ValueError('It is not possible to multiply matrixes with different A_n_columns and B_n_rows.')
        
        result = Matrix(matrix_list=[])

        for A_row in self.matrix:
            result.matrix.append([])

            for B_columns_count in range(len(other.matrix[0])):
                B_column = [row[B_columns_count] for row in other.matrix]
                
                multiplication = 0
                for value_index in range(len(A_row)):
                    multiplication += A_row[value_index] * B_column[value_index]

                result.matrix[-1].append(multiplication)

        return result

    def __imul__(self, other):
        if type(other) is not Matrix:
            raise TypeError('It is not possible to multiply a matrix with an object that is not a matrix.')

        if len(self.matrix) != len(other.matrix[0]) and len(other.matrix) != len(self.matrix[0]): 
            raise ValueError('It is not possible to multiply matrixes with different A_n_columns and B_n_rows.')
        
        result = Matrix(matrix_list=[])

        for A_row in self.matrix:
            result.matrix.append([])

            for B_columns_count in range(len(other.matrix[0])):
                B_column = [row[B_columns_count] for row in other.matrix]
                
                multiplication = 0
                for value_index in range(len(A_row)):
                    multiplication += A_row[value_index] * B_column[value_index]

                result.matrix[-1].append(multiplication)

        return result