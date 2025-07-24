file= str(input('Enter file name:'))
file_lower = file.lower()

if file_lower.endswith('.gif'):
    print('image/gif')
elif file_lower.endswith('.jpg') or file_lower.endswith('.jpeg'):
    print('image/jpeg')
else:
    print('application/octet-stream')
