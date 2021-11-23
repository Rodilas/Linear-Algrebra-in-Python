# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:17:57 2021

@author: emile
"""

import math

# ------------ VECTORS ------------

class Vector:
    # Temporary constructor before implementing reading of files
    def __init__(self, inputVector):
        self.vector = inputVector
        self.length = len(inputVector)
    
    def __getitem__ (self, index):
        return self.vector[index]

    def __str__ (self):
        return str(self.vector)
    
    # Adding vectors
    def __add__(self, other):
        assert isinstance(other, Vector)
        v = []
        for i in range (self.length):
            v.append(self.vector[i] + other.vector[i])
        return v
        
    # Multiplying integers and floats with vectors
    def __mul__(self, other):
        isinstance(other, (int,float))
        newVector = [0] * self.length
        for i in range(self.length):
            newVector[i] = other * self.vector[i]
        return Vector(newVector)

    def __rmul__(self, other):
        return self.__mul__(other)
    
    # Inner product
    def innerProduct(self, other):
        assert isinstance(other, Vector)
        som = 0
        for i in range(len(self.vector)):
            som += self.vector[i] * other.vector[i]
        return som

    # Cross product
    def vectorLength(self):
        sqrd_length = 0
        for i in range(self.length):
            sqrd_length += self.vector[i]**2
        return math.sqrt(sqrd_length)

    def crossProduct(self, other):
        if len(self.vector) == 3 and len(other.vector) == 3:
            c1 = self.vector[1]*other.vector[2] - self.vector[2]*other.vector[1]
            c2 = -(self.vector[0]*other.vector[2] - self.vector[2]*other.vector[0])
            c3 = self.vector[0]*other.vector[1] - self.vector[1]*other.vector[0]
            return Vector([c1, c2, c3])
        else:
            print("Cross product is not defined for these vector dimensions")

# Testing creating an object of Vector
a = Vector([1, 2, 3])
b = Vector([4, 5, 6])
# ------------ MATRICES ------------

class Matrix:
    # Temporary constructor before implementing reading of files
    def __init__(self, inputMatrix):
        self.matrix = inputMatrix
        self.col = len(inputMatrix[0])
        self.row = len(inputMatrix)

    def __str__(self):
        s = ""
        for r in range(self.row):
            s += str(self.matrix[r])
            if r < (self.row - 1):
                s += "\n"
        return s

    def transposition (self):
        transposed = [[self.matrix[j][i] for j in range(self.row)] for i in range(self.col)]
        for self.row in transposed:
            print(self.row)
            
            
    def multiplication(self, other):
    
        mult= [[0 for i in range(self.col)] for j in range(other.row)]
        
        if self.col == other.row:
      
            for i in range(self.row):
                for j in range(other.col):
                    for k in range(self.col):
                        mult[i][j] += self.matrix[i][k] * other.matrix[k][j]
            print(mult)            
            
        else:
            return print("Colum of first matrix different from rows of second matrix")        
# Tasks:
# Adding/subtracting matrices --> Alexis
# Multiplying matrices by integers/floats --> Alexis
# Multiplying matrices --> Rodrigo
# Transposing matrices --> João S
# Row-reducing matrices --> Oscar
# Computing the determinant --> Emil

# Testing creating an object of Matrix


a = Matrix([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
b = Matrix([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])


"""
print(a)
print(a.row)
print(a.col)
print(a.transposition())

"""

print(a.multiplication(b))