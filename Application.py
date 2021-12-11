from Classes import Vector, Matrix, LinearSystemSolver


# Question 1:
print("\n")
print("--------------Question 1------------------")
print("\n")
m1 = Matrix([[1, 1, 1], 
             [10, 4, 2], 
             [0, 1, 1]])

v1 = Vector([5.8, 40, 2.75])

c = LinearSystemSolver(m1, v1)
solution1 = c.solve()
product_names1 = ["wheat", "potatoes", "carrots"]
product_profit1 = [50, 100, 100]
profit1 = 0

for i in range (len(solution1)):
    profit1 += product_profit1[i]*round((solution1[i][0]),5)
    print("The farmer produces", round((solution1[i][0]),5),"tons of " + product_names1[i])

print("The farmer profits", profit1)
print("\n")
print("--------------Question 2------------------")
print("\n")       

# Question 2:
m2 = Matrix([[1, 1, 1, 1], 
             [10, 4, 2, 5], 
             [0, 1, 1, 0],
             [0.5,-0.5,-0.5,-0.5]])

v2 = Vector([5.8, 40, 2.75, 0])


c = LinearSystemSolver(m2, v2)
solution2 = c.solve()
product_names2 = ["wheat", "potatoes", "carrots", "Cauliflower"]
product_profit2 = [50, 100, 100, 200]
profit2 = 0

for i in range (len(solution2)):
    profit2 += product_profit2[i]*round((solution2[i][0]),5)
    print("The farmer produces", round((solution2[i][0]),5),"tons of " + product_names2[i])

print("The farmer profits", profit2)

if profit2 > profit1:
    print("The farmer's profit increased by", profit2-profit1)
else:
    print("The farmer's profit decreased by", profit1-profit2)

if solution2[0][0] > solution1[0][0]:
    print("The government's new measure was successful! It increased wheat production by", solution2[0][0] - solution1[0][0])
else:
    print("The government's new measure was not successful! It decreased wheat production by", round((solution1[0][0]-solution2[0][0]),5), "tons")





"""a2 = Matrix([[1,1,1,0,0,0,0,0,0,0],
             [0,0,0,1,1,1,0,0,0,0],
             [0,0,0,0,0,0,1,1,1,1],
             [1,0,0,1,0,0,1,0,0,0],
             [0,1,0,0,1,0,0,1,0,0],
             [0,0,1,0,0,1,0,0,1,0],
             [500,700,600,0,0,0,0,0,0,0],
             [0,0,0,500,700,600,0,0,0,0],
             [0,0,0,0,0,0,500,700,600,600],
             [(1/15),(1/15),(1/15),0,0,0,(-1/18),(-1/18),(-1/18),(-1/18)],
             ])

b2 = Vector([15,25,18,8,10,30,8500,15300,10200,0])

c = LinearSystemSolver(a2, b2)

weights = c.solve()

print(weights)"""