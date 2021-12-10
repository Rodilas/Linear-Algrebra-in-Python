from Classes import Vector, Matrix, MatrixReader, LinearSystemSolver

#A farmer wants to know how many acres of Wheat, Corn and Cauliflower he should grow.

a = Matrix([[1, 1, 1], 
             [10, 4, 2], 
             [0, 1, 1]])

b = Vector([5.8, 40, 2.75])







a2 = Matrix([[1,1,1,0,0,0,0,0,0,0],
             [0,0,0,1,1,1,0,0,0,0],
             [0,0,0,0,0,0,1,1,1,1],
             [1,0,0,1,0,0,1,0,0,0],
             [0,1,0,0,1,0,0,1,0,0],
             [0,0,1,0,0,1,0,0,1,0],
             [500,700,600,0,0,0,0,0,0,0],
             [0,0,0,500,700,600,0,0,0,0],
             [0,0,0,0,0,0,500,700,600,0],
             [(1/15),(1/15),(1/15),0,0,0,(-1/18),(-1/18),(-1/18),0],
             ])

b2 = Vector([15,25,18,8,10,30,8500,15300,10200,0])

c = LinearSystemSolver(a2, b2)

weights = c.solve()

print(weights)