class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, list)) for list in self.matrix])


    def __add__(self, other):
        result = []
        numbers = []
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    summa = other.matrix[i][j] + self.matrix[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.matrix):
                        result.append(numbers)
                        numbers = []
        else:
            print("Размер матриц не совпадает")
        return Matrix(result)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
matrix_3 = matrix_1 + matrix_2
print(matrix_3)