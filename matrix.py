# My Github: https://github.com/Guilherme-De-Marchi

from random import random
from math import e as eulers_number

class Matrix:
    def __init__(self, n_rows=1, n_columns=1, matrix_list='random'):
        ''' Configurations: random -> random values ​​for the matrix
            or insert a list to use it.'''
        
        if matrix_list == 'random':
            self.matrix = [[random() for column in range(n_columns)] for row in range(n_rows)]

        elif type(matrix_list) == list:
            self.matrix = matrix_list

        else:
            raise ValueError('Matrix "matrix_list" argument incorrect.')

    def __str__(self): return f'{self.matrix}'

    def __add__(self, other):
        if type(other) not in [Matrix, int, float]:
            raise TypeError('It is not possible to add a matrix to an object that is not a matrix.')

        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]): 
            raise ValueError('It is not possible to add matrices with different sizes.')

        result = Matrix(matrix_list=[])

        for index_row in range(len(self.matrix)):
            result.matrix.append([])

            for index_column in range(len(self.matrix[index_row])):
                result.matrix[-1].append(self.matrix[index_row][index_column] + other.matrix[index_row][index_column])

        return result

    def __iadd__(self, other): return self.__add__(other)

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

    def __isub__(self, other): return self.__sub__(other)

    def __mul__(self, other):
        if type(other) not in [Matrix, int, float]:
            raise TypeError('It is not possible to multiply a matrix with an object that is not a matrix or a number.')

        result = Matrix(matrix_list=[])

        if type(other) is Matrix:
            if len(self.matrix) != len(other.matrix[0]) and len(other.matrix) != len(self.matrix[0]): 
                raise ValueError('It is not possible to multiply matrixes with different A_n_columns and B_n_rows.')

            for A_row in self.matrix:
                result.matrix.append([])

                for B_columns_count in range(len(other.matrix[0])):
                    B_column = [row[B_columns_count] for row in other.matrix]
                    
                    multiplication = 0
                    for value_index in range(len(A_row)):
                        multiplication += A_row[value_index] * B_column[value_index]

                    result.matrix[-1].append(multiplication)

        else:
            for row in self.matrix:
                result.matrix.append([])

                for number in row:
                    result.matrix[-1].append(number*other)

        return result

    def __imul__(self, other): return self.__mul__(other)

    def transpose(self):
        result = Matrix(matrix_list=[])

        for column in range(len(self.matrix[0])):
            result.matrix.append([])

            for row in range(len(self.matrix)):
                result.matrix[-1].append(self.matrix[row][column])

        return result

    def sigmoid(self):
        result = Matrix(matrix_list=[])

        for row in self.matrix:
            result.matrix.append([])

            for number in row:
                result.matrix[-1].append(1 / (1 + eulers_number ** -number))

        return result

    def derivative_sigmoid(self):
        result = Matrix(matrix_list=[])

        for row in self.matrix:
            result.matrix.append([])

            for number in row:
                result.matrix[-1].append(number * (1 - number))

        return result

    @staticmethod
    def hadamard(first_object, second_object): 
        if type(second_object) is not Matrix:
            raise TypeError('it is not possible to calculate the hadamart product between a matrix and an object that is not a matrix.')

        if len(first_object.matrix) != len(second_object.matrix) or len(first_object.matrix[0]) != len(second_object.matrix[0]): 
            raise ValueError('it is not possible to calculate the hadamart product between matrices of different sizes.')

        result = Matrix(matrix_list=[])

        for row in range(len(first_object.matrix)):
            result.matrix.append([])
            
            for column in range(len(first_object.matrix[row])):
                result.matrix[-1].append(first_object.matrix[row][column] * second_object.matrix[row][column])

        return result
