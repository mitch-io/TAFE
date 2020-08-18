# Method to return a shortened string
def shortString(inText, length):
    outText = str()
    i = 0
    if len(text) <= length:
        outText = inText
        return outText
    else:
        for x in range(0, length):
            outText = outText + inText[i]
            i += 1
        return outText

# Get user input
text = input('Please enter a word: ')
num = int(input('Please enter a number: '))

# Print output 
print(shortString(text, num))