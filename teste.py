# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:33:54 2021

@author: rodri
"""



with open("matrix_file_10.txt", 'r') as f:
       
    MatrixDimension = f.readline()
    NonZeroEntries = f.readline()
    print(MatrixDimension)
    print(NonZeroEntries)
    f_file= f.read()
    print(f_file, end = "")



"""

#soma de vetores
a = [3, 5, -5, 8]
b = [4, 7, 9, -4]

print("Vector a = ", a)
print("Vector b = ", b)

#soma de vetores
sum = []
for i in range(len(a)):
    sum.append(a[i] + b[i])

print("Vector Addition = ", sum)


"""

#multiplicar vector por integer/float


"""

a = [1, 2, 3]
n = 2.1

Mult = []
for j in range(len(a)):
    Mult.append(a[j]*n)
    
print(Mult)    

"""


#inner product

"""

a = [1, 2, 3]
b = [4, 5, 6]
#32
soma= 0
for i in range(len(a)):
    
    soma += a[i]*b[i]
    
print(soma)

"""
#cross product

"""

a = [1, 2, 3]
b = [4, 5, 6]

Mult = []

for i in range(len(a)):
    Mult.append(0)
    for j in range(len(a)):
        if j != i:
            for k in range(len(a)):
                if k != i:
                    if k > j:
                        Mult[i] += a[j]*b[k]
                    elif k < j:
                        Mult[i] -= a[j]*b[k]
print(Mult)
        
"""

#matrices


"""

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)

"""




