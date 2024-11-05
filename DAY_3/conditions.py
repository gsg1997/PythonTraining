def oddeven(num): 
    if num%2==0:
        return "EVEN"
    else:
        return "ODD"
print("Enter Number: ")
number=int(input())
print("your number is: ",oddeven(number))

