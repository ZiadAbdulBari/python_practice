#Problem: 01
# num = int(input("Enter a number: "))
# if(num%2==0):
#     print("Even number")
# else:
#     print("Odd number")

#Problem: 02
first_number = int(input("First number: "))
second_number = int(input("Second number: "))
operator = input("Take an operator: ")
if(operator=="+"):
    print(first_number+second_number)
elif(operator=="-"):
    print(first_number-second_number)
elif (operator=="*"):
    print(first_number*second_number)
else:
    print(first_number/second_number)
