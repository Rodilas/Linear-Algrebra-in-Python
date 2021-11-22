# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:17:57 2021

@author: emile
"""

import math

class Vector:
    # Temporary constructor before implementing reading of files
    def __init__(self, inputVector):
        self.vector = inputVector
    
    def __len__(self):
        return len(self.vector)
    
    def __getitem__ (self, index):
        return self.vector[index]

    def __str__ (self):
        return str(self.vector)
    
    # Adding vectors
    def __add__(self, other):
        assert isinstance(other, Vector)
        for i in range (0, len(self.vector)):
            self.vector[i] += other.vector[i]
        return self.vector
        
    # Multiplying integers and floats with vectors
    def __mul__(self, other):
        isinstance(other, (int,float))
        newVector = [0] * len(self.vector)
        for i in range(len(self.vector)):
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
        for i in range(len(self.vector)):
            sqrd_length += self.vector[i]**2
        return math.sqrt(sqrd_length)

    def crossProduct(self, other):
        if len(self.vector) == 3 and len(other.vector) == 3:
            True

# Testing creating an object of Vector
a = Vector([1, 2, 3])
b = Vector([4, 5, 6])