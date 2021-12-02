from LinAlgAssignment import Vector, Matrix, MatrixReader, LinearSystemSolver

# Temporary setup. We need to figure out want kind of application the professor wants.


file = "Matrix_file_" + str(input("Choose matrix dimension (10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120): ")) + ".txt"
reader = MatrixReader(file)
m = Matrix(reader.load())
print(m)