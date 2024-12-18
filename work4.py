print("Task 1")
print(" ")

len_one = int(input("Enter length list: "))

first_list = []

for i in range(len_one):
    val_one = int(input(f"Enter value for element {i+1}: "))  
    first_list.append(val_one)

print(first_list, "- list")


sum = 0  

for i in range(len_one):
    if i == 0 or i % 2 == 0:  
        val_onee = first_list[i]
        sum += val_onee

answer = sum * first_list[len_one - 1]

print(answer)