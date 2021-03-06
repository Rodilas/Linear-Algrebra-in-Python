# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:17:57 2021

@author: emile
"""

import math

# ------------ VECTORS ------------

class Vector:
    def __init__(self, inputVector):
        self.length = len(inputVector)
        self.vector = []
        for i in range(self.length):
            self.vector.append(inputVector[i])
    
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
        return Vector(v)
        
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

    #Magnitude/Length of vector
    def vectorLength(self):
        sqrd_length = 0
        for i in range(self.length):
            sqrd_length += self.vector[i]**2
        return math.sqrt(sqrd_length)
    
    # Cross product
    def crossProduct(self, other):
        if (self.length) == 3 and (other.length) == 3:
            return Vector([(self.vector[1]*other.vector[2] - self.vector[2]*other.vector[1]), 
                           -(self.vector[0]*other.vector[2] - self.vector[2]*other.vector[0]), 
                           (self.vector[0]*other.vector[1] - self.vector[1]*other.vector[0])])
        else:
            print("Cross product is not defined for these vector dimensions")



# ------------ MATRICES ------------

class Matrix:
    def __init__(self, inputMatrix):
        self.col = len(inputMatrix[0])
        self.row = len(inputMatrix)
        self.matrix = [[0 for i in range(self.col)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j] = inputMatrix[i][j]
        
        for i in range(self.row):
            for j in range(1, self.row):
                assert len(inputMatrix[i]) == len(inputMatrix[j])

    def __str__(self):
        s = ""
        for r in range(self.row):
            s += str(self.matrix[r])
            if r < (self.row - 1):
                s += "\n"
        return s
    
    def __add__(self, other):
       
        add = [[0 for i in range(self.col)] for j in range(other.row)]
        
        if self.col == other.col and self.row == other.row:
            
            for i in range(self.row):
                for j in range(other.col):
                    add[i][j] = self.matrix[i][j] + other.matrix[i][j]
                    
            return Matrix(add)
    
    def __sub__(self, other):
        sub = [[0 for i in range(self.col)] for j in range(other.row)]

        if self.col == other.col and self.row == other.row:
            
            for i in range(self.row):
                for j in range(other.col):
                    sub[i][j] = self.matrix[i][j] - other.matrix[i][j]
            
            return Matrix(sub)
        
    def __mul__(self, other):
        if isinstance(other, (int,float)) == True:
            mult = [[0 for i in range(self.col)] for j in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    mult[i][j] = self.matrix[i][j] * other
            return Matrix(mult)
       
        else:
            mult = [[0 for i in range(other.col)] for j in range(self.row)]

            if self.col == other.row:
                for i in range(self.row):
                    for j in range(other.col):
                        k = 0
                        for k in range(other.row):
                            mult[i][j] += self.matrix[i][k] * other.matrix[k][j]
                        
                return Matrix(mult)            
                                                         
            else:
                print("Colum of first matrix different from rows of second matrix")
    
    def __rmul__(self, other):
        isinstance(other, (int,float))
        return self.__mul__(other)
   
    def __getitem__(self, index):
        return self.matrix[index]
    
    def __len__(self):
        return len(self.matrix)

    def transpose (self):
        temp = self.matrix
        transposed = [[temp[j][i] for j in range(self.row)] for i in range(self.col)]
        return Matrix(transposed)

    def symmetrical (self):
        if self.transpose() == self.matrix:
            return True
        else:
            return False   

    def rowReduction(self):
        # This method performs row reduction and returns a matrix in row echolon form
        h = 0
        k = 0
        tempMatrix = Matrix(self.matrix)
        row = tempMatrix.row
        col = tempMatrix.col
        swapRowCounter = 0

        while h < row and k < col:
            # Finding index of maximum absolute value
            imax = 0
            tempMax = 0
            for i in range(h, row):
                if abs(tempMatrix.matrix[i][k]) > tempMax:
                    imax = i
                    tempMax = abs(tempMatrix.matrix[i][k])
            
            if tempMatrix.matrix[imax][k] == 0:
                # No pivot in this column, move on to the next
                k += 1
            else:
                self.__swapRows(tempMatrix.matrix, h, imax)
                swapRowCounter += 1
                for x in range(h+1, row):
                    f = tempMatrix.matrix[x][k] / tempMatrix.matrix[h][k]
                    tempMatrix.matrix[x][k] = 0
                    for y in range(k+1, col):
                        tempMatrix.matrix[x][y] = (tempMatrix.matrix[x][y] - f*tempMatrix.matrix[h][y])
                h += 1
                k += 1
        
        return [tempMatrix, swapRowCounter]
    
    # Private method used in row reduction
    def __swapRows(self, matrixToSwap, i1, i2):
        tempRow = matrixToSwap[i1]
        matrixToSwap[i1] = matrixToSwap[i2]
        matrixToSwap[i2] = tempRow

    #Method for extracting "c"th column (in vector form)
    def getCol(self, c):
        tempCol = []
        for i in range(self.col):
            tempCol.append(self.matrix[i][c-1])
        return Vector(tempCol) 
        
    #Determinant method
    def determinant(self):
        reducedMatrix = self.rowReduction()[0]
        swaps = self.rowReduction()[1]
        if reducedMatrix.row == reducedMatrix.col:
            det = reducedMatrix.matrix[0][0]
            if self.col % 2 != 0:
                for i in range(1, reducedMatrix.row):
                    det *= reducedMatrix.matrix[i][i]
                return det * (-1 ** swaps)
            else:
                for i in range(1, reducedMatrix.row):
                    det *= reducedMatrix.matrix[i][i]
                return det * (-1 ** (swaps - 1))
        else:
            print("Only square matrices may have determinants, this matrix is not square.")


#------------- LOADING THE FILE ----------------

class MatrixReader:
    def __init__(self, filename):
        self.filename = filename
    
    def load(self):
        f=open(self.filename, 'r')
        n= f.readline() #reads first line for dimension
        s = n.split()   #splits the first line
        num= int(s[2])+ 1 #gets matrix dimension, int is because split reads as a char
            
        f.readline() #useless line
            
        matrice = []  #store matrix here
            
        line = f.readline().split()
        for i in range(num): #rows
            rows = [] #each row
            for j in range(num): #col
                row, col, val = int(line[0]), int(line[1]), float(line[2])  #basically each of the next lines of the file format
                if row == i and col == j : #checks to see if its 0 entry or not
                    rows.append(val) #add value to row
                    line = f.readline().split() #loop entry
                else:
                    rows.append(0)
                        
            matrice.append(rows) #add 10 by 10 to matrix
        f.close()
        return matrice


class VectorReader:
    def __init__(self, filename):
        self.filename = filename
    
    def load(self):
        f=open(self.filename, 'r')
        vector_row = eval(input("Insert vector row, has to be smalller then the matrix dimension:"))
        dimension = eval(input("Insert vector dimension, has to be smalller then the matrix dimension:"))
        n= f.readline() #reads first line for dimension
        s = n.split()   #splits the first line
        num= int(s[2])+ 1 #gets matrix dimension, int is because split reads as a char
            
        f.readline() #useless line
        if vector_row > num :
            return "Vector_row to big for the file"
        elif dimension > num:
            return "Dimension to big for the file"
        Vector = [0 for _ in range(dimension)] #initialize vector as zeroes
        line = f.readline()
        while line:
            parts = line.split()
            row, col, val = int(parts[0]), int(parts[1]), float(parts[2])  #basically each of the next lines of the file format
            if row > vector_row or (row == vector_row and col >= dimension): #break the cycle if we passed requested row or at requested row and passed dimension
                break
            if row == vector_row: #set vector value if we are at requested row
                Vector[col] = val
            line = f.readline() #loop entry
        
        f.close()
        return Vector


# ------------ SOLVING LINEAR SYSTEM ------------

class LinearSystemSolver:
    def __init__(self, inputMatrix, inputVector):
        self.a = inputMatrix
        self.b = inputVector
        self.dim = len(inputMatrix.matrix)

    def solve(self):
        # Merging the A matrix with the B vector
        mergedMatrix = [[0 for j in range(self.dim + 1)] for i in range(self.dim)]
        for r in range(self.dim):
            for c in range(self.dim + 1):
                if c < (self.dim):
                    mergedMatrix[r][c] = self.a.matrix[r][c]
                else:
                    mergedMatrix[r][c] = self.b.vector[r]

        # Row reduction
        m = Matrix(mergedMatrix)
        m = m.rowReduction()[0]
        m = m.matrix

        # Calculation xn
        result = [0]*self.dim
        result[self.dim-1] = m[self.dim-1][self.dim]/m[self.dim-1][self.dim-1]

        # Calculating x1 --> xn-1
        for i in range(self.dim-2, -1, -1):
            sum = 0
            for j in range(i+1, self.dim):
                sum += m[i][j]*result[j]
            result[i] = (m[i][self.dim] - sum)/m[i][i]

        # Returning a one column matrix
        resultMatrix =[]
        for r in result:
            resultMatrix.append([r])
        return Matrix(resultMatrix)

    