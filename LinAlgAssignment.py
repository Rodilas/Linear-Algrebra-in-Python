# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:17:57 2021

@author: emile
"""

class vector:
    def __init__(self, elements=[]):
        assert isinstance(elements, list)
        self.velements = elements
    
    def setElements(self, v):
        assert isinstance(v, list)
        for i in range(len(v)):
            assert isinstance(v[i], (float, int))            
        self.velements = self.velements.extend(v)
    
    def __str__(self):
        return print(self.velements)
    
v1 = vector()

v1.setElements([1,2,3])


