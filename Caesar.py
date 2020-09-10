import sys
# Author: Andrew Mitchell
# Date: 02 August 2020

encrypt_output = ""

#function to convert the user’s input into something suitable to be encrypted
def convert_to_Caesar(input_str):
    #declare a list ready for the output
    output_list = []
    #iterate through input string
    for char in input_str:
        #replace . with X and appent to output list
        if char == '.':
            output_list.append('X')
        elif char.isalpha() == True:
            #append only alphabet characters to output list and make them UPPERCASE
            output_list.append(char.upper())
    #function returns output list
    return ''.join(output_list)

#function for encryption
def encrypt_Caesar(input_str, input_shift):
    #declare a list ready for the output
    output_list = []
    #convert str to int
    shift_numb = int(input_shift)
    #iterate through input string
    for char in input_str:
        # Shift by input_shift
        output_list.append(chr((ord(char) + shift_numb - 65) % 26 + 65))
    #function returns output list
    return ''.join(output_list)

#function for help
def help_Caesar():
    print('\n For full documentation please see www.readme.com')
    print('\n The action of a Caesar cipher is to replace each plaintext letter')
    print(' with a different one a fixed number of places down the alphabet.')
    print('\n To run interactively:')
    print(" [+] ICTPRG405_AT1_Task3_amitchell.py without any arguments")
    print('\n Command line arguments:')
    print(" [+] ICTPRG405_AT1_Task3_amitchell.py '?' FOR HELP")
    print(' [+] ICTPRG405_AT1_Task3_amitchell.py {sting to encrypt/decrypt} {positive integer to encrypt/negative integer to decrypt}')
    print(' [+] Example input: ICTPRG405_AT1_Task3_amitchell.py iuhdfuhfguh58%&gVF 3')
    print(' [+] Example output: LXKGIXKIJXKJYI')
    print(' [+] NB. If your string to be encrypted has spaces in it please put it within "speech marks"')
    input()

inProgress = False
# check whether to do commandline arguments or run program
if len(sys.argv) > 2:
    # Need logic for help and error checking
    if sys.argv[1] == '?':
        help_Caesar()
        #inProgress = False
    elif sys.argv[2].lstrip('-').isdigit() != True:
        print("**ERROR - Whole number required for second argument, '?' FOR HELP**")
    else:
        caesar_str = convert_to_Caesar(sys.argv[1])
        print(encrypt_Caesar(caesar_str, int(sys.argv[2])))
        #inProgress = False
    #inProgress = False
    
elif len(sys.argv) == 2:
    if sys.argv[1] == '?':
        help_Caesar()
        #inProgress = False
    else:
        print("**ERROR - Two arguments required, '?' FOR HELP**")
        #inProgress = False
else:
    inProgress = True

while inProgress == True:
    # print welcome message
    print('Options: \n 1. Encrypt \n 2. Decrypt \n 3. Help \n 4. Exit')
    selection = input('> ')
    # loop until a number betweeon 1 and 4 is entered
    while selection.lstrip('-').isdigit() != True or selection > "4":
        selection = (input('ERROR: \n 1. Encrypt \n 2. Decrypt \n 3. Help \n 4. Exit \n > '))

    # select 1 - encrypt 
    if int(selection) == 1:
        input_str = input('Enter a word: ')
        caesar_str = convert_to_Caesar(input_str)
        input_shift = input('Please enter a number: ')
        # loop until a number is entered
        while input_shift.lstrip('-').isdigit() != True:
            input_shift = (input('ERROR - Please enter a whole number: '))
        encrypt_output = encrypt_Caesar(caesar_str, int(input_shift))
        print('Encrypted string: ' + encrypt_output)
        print()

    # select 2 - decryption
    if int(selection) == 2:
        # if string was previously encrypted you get the option to decrypt it automatically
        if encrypt_output != "":
            print('Would you like to decrypt the previously encrypted string: ' + encrypt_output + ' ?')
            print('Options: \n 1. Yes \n 2. No')
            selection = input('> ')
            while selection.lstrip('-').isdigit() != True or selection > "2":
                selection = (input('ERROR: \n 1. Yes \n 2. No \n > '))
            if selection == '1':
                caesar_str = encrypt_output
                decrypt_output = encrypt_Caesar(caesar_str, -int(input_shift))
                print('Decrypted string: ' + decrypt_output)
                print()
            # if the user doesn't want to decrypt the previously encrypted string
            elif selection == '2':
                input_str = input('Enter a word: ')
                caesar_str = convert_to_Caesar(input_str)
                input_shift = input('Please enter a number: ')
                while input_shift.lstrip('-').isdigit() != True:
                    input_str = (input('ERROR - Please enter a whole number: ')) 
                decrypt_output = encrypt_Caesar(caesar_str, -int(input_shift))
                print('Decrypted string: ' + decrypt_output)
                print()
        # if string wasn't previously encrypted
        else:
            input_str = input('Enter a word: ')
            caesar_str = convert_to_Caesar(input_str)
            input_shift = input('Please enter a number: ')
            while input_shift.lstrip('-').isdigit() != True:
                input_str = (input('ERROR - Please enter a whole number: ')) 
            decrypt_output = encrypt_Caesar(caesar_str, -int(input_shift))
            print('Decrypted string: ' + decrypt_output)

    # select 3 - show help
    if int(selection) == 3:
        help_Caesar()
        
    # select 4 - exit
    if int(selection) == 4:
        inProgress = False