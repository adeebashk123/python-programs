matrix1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix1)

print(matrix1[0])
print(matrix1[0][1])

for r in matrix1:
    print()
    for item in r:
        print(item, end=' ')
        
#addition of two matrix
m1=[
    [1,2],
    [3,4]
]
m2=[
    [5,6],
    [7,8]
]
result=[
    [0,0],
    [0,0]
]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        result[i][j]=m1[i]+[j]+m2[i][j]
        print(result[i][j],end=" ")
    
    