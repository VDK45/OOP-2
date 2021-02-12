class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        new_m = []
        for i in range(len(self.matrix)):
            new_m.append([])
            for d in range(len(self.matrix[i])):
                new_m[i].append(self.matrix[i][d] + other.matrix[i][d])
        return Matrix(new_m)

    def __str__(self):
        new_m = []
        for i in range(len(self.matrix)):
            for d in range(len(self.matrix[i])):
                new_m.append(f"{self.matrix[i][d]}\t")
            new_m.append("\n")
        return f'{"".join(new_m)}'


a = Matrix([[1, 2], [4, 5], [7, 8]])
print(a)
b = Matrix([[8, 7], [5, 4], [2, 1]])
print(b)
print(a + b)
