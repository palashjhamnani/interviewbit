def printSpiral(A, m, n):
    final = []
    direction = 0
    top = 0
    bottom = m-1
    left = 0
    right = n-1
    while (top<=bottom and left<=right):
        if direction==0:
            for i in range (left, right+1):
                final.append(A[top][i])
            top = top+1
            direction = 1
        elif direction == 1:
            for i in range (top, bottom+1):
                final.append(A[i][right])
            right = right-1
            direction = 2
        elif direction == 2:
            for i in range (right, left-1, -1):
                final.append(A[bottom][i])
            bottom = bottom-1
            direction = 3
        elif direction == 3:
            for i in range (bottom, top-1, -1):
                final.append(A[i][left])
            left = left+1
            direction = 0
    print final

A = [[1,2,3],[4,5,6],[7,8,9],[12,13,14]]
m=4
n=3
printSpiral(A, m, n)

            
    
