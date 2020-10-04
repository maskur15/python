#transponse matrix
transponsed =[]
matrix=[[1,2,3,4],[4,5,6,8]]
for i in range(len(matrix[0])):
    transponsed_row=[]
    for row in matrix:
        transponsed_row.append(row[i])
    transponsed.append(transponsed_row);
print(transponsed)