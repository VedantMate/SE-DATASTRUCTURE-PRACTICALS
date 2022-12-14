# Experiment No. 8 : Write a Python program that determines the location of a saddle point of matrix if one
#                    exists. An m x n matrix is said to have a saddle point if some entry a[i][j] is the smallest
#                    value in row i and the largest value in j.

def findSaddlePoint(mat, n):
    
	for i in range(n):

		min_row = mat[i][0]
		col_ind = 0
		for j in range(1, n):
			if (min_row > mat[i][j]):
				min_row = mat[i][j]
				col_ind = j

		k = 0
		for k in range(n):

			if (min_row < mat[k][col_ind]):
				break
			k += 1

		if (k == n):
			print("Value of Saddle Point ",
				min_row)
			return True

	return False

if __name__ == '__main__':

	mat = [[1, 2, 3],
		  [4, 5, 6],
	   	  [7, 8, 9]]

	n = 3
	if (findSaddlePoint(mat, n) ==
		False):
		print("No Saddle Point");
