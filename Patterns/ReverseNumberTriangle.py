def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    for row in range(1,n+1):
        for col in range(1,n-row+1+1):
            print(col,end=' ')

        print()
    pass