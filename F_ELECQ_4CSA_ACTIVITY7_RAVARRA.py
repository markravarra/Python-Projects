#F_ELECQ_4CSA_ACTIVITY7_RAVARRA
import numpy as np

nRow = int(input("Enter the number of rows:")) 
nCol = int(input("Enter the number of columns:")) 
  
  
print("\nEnter the entries of Matrix A(LHS): ")

arr = []
print('Enter coefficients of the LHS per Equations separated by spaces: ')
for i in range(nRow):
    holder = input("Equation " + str(i+1) +":")
    temparr = list(map(int, holder.split())) 
    arr.append(temparr)
  
# For printing the matrix 
matrixA = np.array(arr).reshape(nRow, nCol) 
print("\nMatrix A:")
print(matrixA)

print("\nEnter the entries of Matrix B(RHS): ")
entries = list(map(int, input("RHS: ").split())) 
matrixB = np.array(entries).reshape(nRow, 1) 
print("\nMatrix B:")
print(matrixB) 

X = np.linalg.inv(matrixA).dot(matrixB)

print("\nAnswer of Operation: ")
print(X)