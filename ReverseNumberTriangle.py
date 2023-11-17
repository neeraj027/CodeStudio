def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    for row in range(n):
        for col in range(n):
            if col<(n-row):
                print(col+1,end=' ')
        print()
    pass