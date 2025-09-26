import random
required_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
required_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
required_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the password generator')
letters= int(input('how many letters ?'))
numbers=int(input('how many numbers ?'))
symbols=int(input('how many symbols ?'))


password=[]
for char in range(0, letters):
    password.append(random.choice(required_letters))
    
for char in range(0, numbers):
    password.append(random.choice(required_numbers))
    
for char in range(0, symbols):
    password.append(random.choice(required_symbols))
    
random.shuffle(password)    
print(password)

password1=''
for char in password:
    password1+=char
print(f'your password is:{password1}')