#import sys (will need sys for argv)
# Author: Andrew Mitchell
# Date:   <date that you wrote the code>

offset = '14354Adg$-35'
numbers = ['-', '1', '2', '3', '4', '5', '6', '7', '8', '9']    
newOffset = list()
i = 0

for char in offset:
    for n in numbers:
        if char == n:
            newOffset.append(char)
        else:
            newOffset.append('')
            
            
print(newOffset)

input_string = 'string'
#alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']