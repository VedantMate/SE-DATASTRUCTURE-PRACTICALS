# Experiment No. 9 : Write a Python Program to compute following computation on matrices :
#                   a)Addition of two matrices
#                   b)Subtraction of two matrices
#                   c)Multiplication of two matrices
#                   d)Transpose of a matix



import numpy

print(" Matrix : \n 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9 \n")

list1 = []
list2 = []

for i in range (0,9):
    element = int(input(f'enter the element {i+1} of matrix 1 : '))
    list1.append(element)

for i in range (0,9):
    element = int(input(f'enter the element {i+1} of matrix 2 : '))
    list2.append(element)

x = numpy.array([[list1[0],list1[1],list1[2]], [list1[3],list1[4],list1[5]], [list1[6],list1[7],list1[8]]])
y = numpy.array([[list2[0],list2[1],list2[2]], [list2[3],list2[4],list2[5]], [list2[6],list2[7],list2[8]]])

print("The element wise addition of matrix is : ")
print(f'{numpy.add(x,y)} \n')

print("The element wise subtraction of matrix is : ")
print(f'{numpy.subtract(x,y)} \n')

print ("The product of matrices is : ")
print (f'{numpy.dot(x,y)} \n')

print("The transpose of matrix 1 is : ")
print(f'{x.T} \n')

print("The transpose of matrix 2 is : ")
print(f'{y.T} \n')