#Experiment No. 9 : Write a Python Program to compute following computation on matrices :
#                   a)Addition of two matrices
#                   b)Subtraction of two matrices
#                   c)Multiplication of two matrices
#                   d)Transpose of a matix



import numpy

x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])

print("The element wise addition of matrix is : ")
print(numpy.add(x, y))

print("The element wise subtraction of matrix is : ")
print(numpy.subtract(x, y))

print ("The product of matrices is : ")
print (numpy.dot(x,y))

print("The transpose of given matrix is : ")
print(x.T)