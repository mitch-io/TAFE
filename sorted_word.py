word = input('Please enter a string: ')

if word != ''.join(sorted(word)):
    print('False')
else:
    print('True')