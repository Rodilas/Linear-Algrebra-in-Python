# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:17:57 2021

@author: emile
"""

class Vector:
    # Temporary constructor before implementing reading of files
    def __init__(self, inputVector):
        self.vector = inputVector
    
    def __len__(self):
        return len(self.vector)
    
    def __getitem__ (self, index):
        return self.vector[index]
    
    def __add__(self, other):
        assert isinstance(other, Vector)
        for i in range (0, len(self.vector)):
            self.vector[i] += other.vector[i]
        return self.vector
            
    def __str__ (self):
        s = str(self.vector)
        return s
        

    def __mul__(self, other):
        isinstance(other, (int,float))
        newVector = [0] * len(self.vector)
        for i in range(len(self.vector)):
            newVector[i] = other * self.vector[i]
        return Vector(newVector)

    def __rmul__(self, other):
        return self.__mul__(other)

# Testing creating an object of Vector
a = Vector([1, 2, 3])
b = Vector([4, 5, 6])





print(a+b)


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






















