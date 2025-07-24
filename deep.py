R = (input('What is  the Great Question of Life, the Universe and Everything?'))
R_lower = R.lower()
if R_lower == '42' or R_lower == 'fourty-two' or R_lower == 'fourty two':
    print('Yes')
else:
    print('No')