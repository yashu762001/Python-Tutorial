list = [1,45,67,2,4,46,56,2,32,434,2,3,5313,24,54657,1323,35634,84757459]

def count(list):
    even=0
    odd=0
    for i in list:
        if(i%2==0):
            even+=1
        else:
            odd+=1

    return even,odd

even,odd = count(list)
print(even,odd)
