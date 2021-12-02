from Classes import Vector, Matrix, MatrixReader, LinearSystemSolver
import random, time

print("------- A * X = B -------")

# Matrix A
file = "Matrix_file_" + str(input("Choose dimension of sample matrix A (10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120): ")) + ".txt"
startTime = time.time()
reader = MatrixReader(file)
a = Matrix(reader.load())

# Matrix X, randomized
x = []
for i in range(a.row):
    x.append([random.randint(0,10)])
x = Matrix(x)
print('\n', end="")
print("Randomized matrix X:")
print('\n', end="")
print(x)

# Finding B by multiplication
b = a*x
print('\n', end="")
print("A * X = ")
print('\n', end="")
print(b)

# Making B a vector and then using linear solution solver
bVector = []
for e in b.matrix:
    bVector.append(e[0])
bVector = Vector(bVector)
l = LinearSystemSolver(a, bVector)
xSolution = l.solve()
print('\n', end="")
print("Matrix X from linear solution:")
print('\n', end="")
print(xSolution)

# Checking if the two X matrices are identical
identical = True
for i in range(x.row):
    if abs(x.matrix[i][0]-xSolution.matrix[i][0]) > 0.0001:
        identical = False
        break

print('\n', end="")
if identical:
    print("-------------LINEAR SOLUTIONS WORKS-------------")
else:
    print("-------------LINEAR SOLUTION DOES NOT WORK-------------")

endTime = time.time()
print('\n', end="")
print("ELAPSED TIME: ", endTime-startTime, "seconds")
