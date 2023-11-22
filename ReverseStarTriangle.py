def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n):
        for j in range(i):
            print('',end=' ')
        for j in range((n-i)*2-1):
            print('*',end='')
        for j in range(i):
            print('',end=' ')
        print()
    pass