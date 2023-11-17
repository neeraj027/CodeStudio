def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    small = float('inf')
    secondSmall = float('inf')
    large = float('-inf')
    secondLarge = float('-inf')

    for i in range(n):
        small = min(small, a[i])
        large = max(large, a[i])

    for i in range(n):
        if (a[i] < secondSmall and a[i] != small):
            secondSmall = a[i]
        if (a[i] > secondLarge and a[i] != large):
            secondLarge = a[i]

    return [secondLarge, secondSmall]