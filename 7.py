# Experiment No. 9 : Write a python Program for magic square. A magic square is an n * n matrix of the integers 1 to n2
#                    such that the sum of each row, column, and diagonal is the same. The figure given below is an example
#                    of magic square for case n=5. In this example, the common sum is 65.
#                             15  8    1  24  17
#                             16  14   7   5  23
#                             22  20  13   6   4
#                              3  21  19  12  10
#                              9   2  25  18  11


#Addition of two matrices 
row = int(input("Enter the number of rows:")) 
col = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrixa = [] 

print("Enter the entries rowwise:") 
  
# For user input 
for i in range(row):          # A for loop for row entries 
    a =[] 
    for j in range(col):      # A for loop for column entries 
         a.append(int(input())) 
    matrixa.append(a)     

 
# For printing first  matrix 
for i in range(row): 
    for j in range(col): 
        print(matrixa[i][j], end = " ")

    print() 


sum1=0 
flag=0 
for j in range(col): 
    sum1+=matrixa[0][j]
    print(matrixa[0][j])
sum2=sum1   
sum1=0 
for i in range(1,row): 
    sum1=0 
    for j in range(col): 
        sum1+=matrixa[i][j]
        print(matrixa[i][j])

    if sum1!=sum2: 
        flag=1

    break 
sum2=0 

if flag==0:    
    for j in range(col): 
        sum2=0 
        for i in range(row): 
            sum2+=matrixa[i][j] 
        if sum1!=sum2: 
            flag=1 
        break 
sum2=0       
if flag==0: 
    for i in range(row): 
        for j in range(col): 
            if i==j: 
                sum2+=matrixa[i][j]


    if sum1!=sum2: 
        flag=1 

j=col-1   
sum2=0 

if flag==0: 
    for i in range(row): 
        sum2+=matrixa[i][j] 
        j=j-1 
   
    if sum1!=sum2 : 
        flag=1 

if flag==0: 
    print("Given Matrix is a Magic Square") 
else:
    print("Given Matrix is not a Magic Square")
