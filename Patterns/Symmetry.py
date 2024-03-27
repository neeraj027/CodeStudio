def symmetry(n: int):
    # Write your solution here.
    for i in range(1, 2*n):
        if i <= n:
            for j in range(i):
                print("*", end=" ")
            for j in range((n-i)*4,0,-1):
                print(end=" ")
            for j in range(i):
                print("*",end=" ")
        elif(n<i and 2*n-i>=0): 
            for j in range(2*n-i):
                print("*",end=" ")
            for j in range(0,(i-n)*4):
                print(end=" ")
            for i in range(2*n-i):
                print("*",end=" ")
        print()
                                
    pass