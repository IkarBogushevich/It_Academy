#HW №2
print("Task 1")

from random import randint

Number_one = randint(0, 100)
Number_two = randint(0, 100)
Number_three = randint(0, 100)

results_one = (Number_one + Number_two + Number_three)/3
print(f"({Number_one} + {Number_two} + {Number_three})/3 = {results_one}")

print(" ")
print("================================================================================")
print(" ")

print("Task 2")

Num_one = randint(1,100)
Num_two = randint(1,10)

print(f'{Num_one},{Num_two}')

del_int = Num_one // Num_two
del_mod = Num_one % Num_two

print(f"{del_int},{del_int}")

print(" ")
print("================================================================================")
print(" ")

print("Task 3")

number = float(input())

print(f"({number:.2f}")
print(round(number))
print(f"{number:011.2f}")