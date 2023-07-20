import np

from matrix_error import SizeMatrixError, SizeMatrixMultError


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'Данная матрица: {self.matrix}'

    def __eq__(self, other):
        if len(self.matrix) != len(other.matrix) or \
                len(self.matrix[0]) != len(other.matrix[0]):
            return False
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != other[i][j]:
                    return False
        return True

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or \
                len(self.matrix[0]) != len(other.matrix[0]):
            raise SizeMatrixError()
        res = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return res

    def __sub__(self, other):
        if len(self.matrix) != len(other.matrix) or \
                len(self.matrix[0]) != len(other.matrix[0]):
            raise SizeMatrixError()
        res = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return res

    def __matmul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise SizeMatrixMultError()
        return np.matmul(self.matrix, other.matrix)


matrix_1 = [[1, 1, 1], [2, 2, 2]]
matrix_2 = [[1, 1, 1], [2, 2, 2]]
matrix_3 = [[1, 5, 1], [2, 3, 2], [3, 0, 3]]
m_1 = Matrix(matrix_1)
m_2 = Matrix(matrix_2)
m_3 = Matrix(matrix_3)

print(m_1.matrix == m_2.matrix)
print(m_1 + m_2)
print(m_1 - m_2)
print(m_1 @ m_3)
print(str(m_2))
