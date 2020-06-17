def fact(n):
    result=1
    if(n<0):
        print("Can't find factorial of a negative number")
    elif(n==0):
        print("1",end=" ");
    else:
        for i in range(2,n+1):
            result*=i

    return result

# a =fact(99999)
# print(a)

