def triangle( n:int) ->None:
    # Write your solution here.
    temp=0
    for i in range(n):
        temp+=1
        for j in range(i+1):
            print(str(temp),end=' ')
            
        print()
    pass