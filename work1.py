print ('Hello world')

print("Pls, write your name")
name = input()
print ("And u surname")
surname = input("ввод фамилии: ")
print('Hello ', name, surname, "! You just delved into Python! Great start!") 
print(f'Hello {name} {surname}, ! You just delved into Python! Great start!') 



text = input('Enter the text: ')
print(text.title())


amount = float(input("Enter the number: "))
if (amount>0):
    formatted_amount = f"{amount:,.2f}" 
    print(formatted_amount)
else: print("Nelzya")