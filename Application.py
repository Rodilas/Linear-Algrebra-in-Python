from Classes import Vector, Matrix, LinearSystemSolver

#Question 1 input
m1 = Matrix([[1, 1, 1], 
             [10, 4, 2], 
             [0, 10, 10]])

v1 = Vector([5.8, 40, 27.5])

c1 = LinearSystemSolver(m1, v1)
solution1 = c1.solve()

#Question 2 input
m2 = Matrix([[1, 1, 1, 1], 
             [10, 4, 2, 5], 
             [0, 10, 10, 0],
             [0.5,-0.5,-0.5,-0.5]])

v2 = Vector([5.8, 40, 27.5, 0])

c2 = LinearSystemSolver(m2, v2)
solution2 = c2.solve()


def main():
    value1 = True
    value2 = True
    
    for i in range(len(solution1)): #if all values in solution vector 1 are positive
        if solution1[i][0] < 0:
            value1 = False

    for i in range(len(solution2)): #if all values in solution vector 2 are positive
        if solution2[i][0] < 0:
            value2 = False

    if value1 == True and value2 == True: #if both solutions return positive values
        return application(solution1, solution2)
    else:
        s5 = print("The solution is not feasible")
        return s5



def application(solution_1, solution_2):
    # Question 1:
    print("\n")
    print("--------------Question 1------------------")
    print("\n")

    product_names1 = ["wheat", "potatoes", "carrots"]
    product_profit1 = [50, 100, 100]
    tons1 = [5, 10, 10]
    profit1 = 0

    for i in range (len(solution1)):
        profit1 += product_profit1[i]*round(((solution1[i][0])*tons1[i]),3)
        print("The farmer produces", round(((solution1[i][0])*tons1[i]),3),"tons of " + product_names1[i])
    print("The farmer profits: ", round((profit1),3))


# Question 2:
    print("\n")
    print("--------------Question 2------------------")
    print("\n")       

    product_names2 = ["wheat", "potatoes", "carrots", "Cauliflower"]
    product_profit2 = [50, 100, 100, 200]
    tons2 = [5, 10, 10, 20]
    profit2 = 0

    for i in range (len(solution2)):
        profit2 += product_profit2[i]*round(((solution2[i][0])*tons2[i]),3)
        print("The farmer produces", round(((solution2[i][0])*tons2[i]),3),"tons of " + product_names2[i])
    print("The farmer profits", round((profit2),3))

    if profit2 > profit1:
        print("The farmer's profit increased by", round((profit2-profit1),3))
    else:
        print("The farmer's profit decreased by", round((profit1-profit2),3))

    if solution2[0][0] > solution1[0][0]:
        print("The government's new measure was successful! The acres the farmer dedicates to wheat reduced by"
              , round((solution2[0][0] - solution1[0][0]),3), "acres.")
    else:
        print("The government's new measure was not successful! \nThe acres the farmer dedicates to wheat reduced by", 
              round((solution1[0][0]-solution2[0][0]),3), "acres.")

main()