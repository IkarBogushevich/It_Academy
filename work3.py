print(" ")
print("================================================================================")
print(" ")

print("Task 1")

num1=int(input("Enter the number: "))

if ((num1 % 5)==0 ) and ((num1 % 3)==0):
    print("Fizz Buzz")
elif ((num1 % 3)==0):
    print("Fizz")
elif ((num1 % 5)==0):
    print("Buzz")
else:
    print(num1)
    
print(" ")
print("================================================================================")
print(" ")

print("Task 2")

num2=int(input("Enter the number: "))
print("Evaluation sheet: ")
print("1. NICEEE")
print("2. Not bad")
print("3. So-so")
print("4. Bad")



match num2:
    case num2 if 2 <= num2 <= 5 and num2 % 2 == 0:
        print("Result: So-so")
    case num2 if 6 <= num2 <= 20 and num2 % 2 == 0:
        print("Result: Not bad")
    case num2 if num2 > 20 and num2 % 2 == 0:
        print("Result: NICEEE")
    case _:
        print("Result: Bad")
        
print(" ")
print("================================================================================")
print(" ")