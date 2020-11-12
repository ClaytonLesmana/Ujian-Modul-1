def hollowTriangle(n):

    for row in range(1,n+1): #1,2,3,4
        for col in range(1,2*n): #1,2,3,4,5,6,7
            if row==n or row+col==n+1 or col-row==n-1: #conditional that will only print # if condition is done
                print('#',end='')
            else:
                print(end='_')
        print()
hollowTriangle(2)