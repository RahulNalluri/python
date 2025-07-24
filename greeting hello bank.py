P = input('Greetings: ')
P_lower = P.lower()
if P_lower.startswith('hello') or P_lower == 'hello , Newman':
    
    print('$0')
elif P_lower.startswith('h'):
    print('$20')
else:
    print('$100')