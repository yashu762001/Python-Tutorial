from array import *
arr = array('i',[])

print("Enter the size of array")
n = int(input())
# Way of taking input from user
for i in range(0,n):
    print("Enter the value")
    x = int(input())
    arr.append(x)

for i in arr:
    print(i,end=" ")

# This input method is used to take user input and it returns a string, but since we want the variable to store a
# integer value so we will need to convert the string into a integer by writing int.
print(" ")
val = int(input("Enter the value you want to search"))
# If array is sorted then use binary search below since it takes logn time else use O(n) for loop to check.
# left = 0
# right = len(arr)-1
# while(left<=right):
#     mid = int((left+right)/2)
#     if(arr[mid]>val):
#         left = mid+1
#         right = right
#
#
#     elif(arr[mid]<val):
#         left = left
#         right = mid-1
#
#
#     elif(arr[mid]==val):
#         print("YES")
#         break;
#
# else:
#     print("NO")
try:
 print(arr.index(val))

except Exception as e:
    print("The number you are searching for does not exist in the given array")

# This is the direct method which provides the index if number is present else throws the error that number not
# found.

# Above is a way of stopping the program from terminating due to rise of exception. You will learn all this in
# Topic Errors.
