#ask user to enter a string
fileName = input('Name of file to reverse: ')

#read file into list varible
with open(fileName, "r") as f:
    text = f.readline()

print('\nOrignal text...')
print(text)

i = len(text) - 1
reverseText = str()

#iterate over text backwards
while i >0:
    reverseText = reverseText + (text[i])
    i -= 1

print('\nText reversed...')
print(reverseText)
f.close()