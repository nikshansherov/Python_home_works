class MatrixError(Exception):
    pass


class SizeMatrixError(MatrixError):
    def __str__(self):
        return 'Для данной операции матрицы должны быть одинакового размера.'


class SizeMatrixMultError(MatrixError):
    def __str__(self):
        return 'Для данной операции количество столбцов первой матрицы\n ' \
               'должно совпадать с количеством строк второй матрицы'
