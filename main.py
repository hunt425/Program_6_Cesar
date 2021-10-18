#########################################
#Hunter Tysdal
#CS101 Lab
#Program_6
#Cesar_Shift_Program

import string

print("Welcome to Caesar Cipher")

def menu():
    print('e = encode a message')
    print('d = decode a message')
    print('q = quit')


def encoding(letter, shift):

    if letter.islower(): #converts upper case strings to lower
        letter = letter.upper()
    elif letter.isupper(): #converts lower case string to upper
        letter = letter.lower()
    new_str = ''
    while shift > 26:
        shift -= 26
    for i in range(len(letter)):
        if letter[i].isalpha():
            char_value = ord(letter[i])
            conversion = chr(char_value + shift)
            if ord(conversion) > 90 and ord(conversion) < 97: #Accounts for non alphabet characters
                move = abs(90 - ord(conversion))
                conversion = chr(64 + move)
            elif ord(conversion) > 122:
                move = abs(122 - ord(conversion))
                conversion = chr(96 + move)
            new_str += conversion #Adds to empty string
        else:
            new_str += letter[i]
    return new_str

def decoding(letter, shift):

    if letter.islower():
        letter = letter.upper()
    elif letter.isupper():
        letter = letter.lower()
    new_str = ''
    while shift > 26:
        shift -= 26
    for i in range(len(letter)):
        if letter[i].isalpha():
            char_value = ord(letter[i])
            conversion = chr(char_value - shift)
            if ord(conversion) < 65:
                move = abs(65 - ord(conversion))
                conversion = chr(91 - move)
            elif ord(conversion) > 90 and ord(conversion) < 97:
                move = abs(122 - char_value)
                conversion = chr(95 + move)
            new_str += conversion
        else:
            new_str += letter[i]
    return new_str



valid = ['e', 'd', 'q']
choice = ''
while choice != 'q':
    menu()
    choice = input('Please enter your choice:\n')
    choice = choice.lower()
    if choice in valid:

        if choice == 'e':
            letter = input('Enter string to encode:\n')
            shift = int(input('Enter amount to shift:\n'))
            print('Original Message: {}'.format(letter))
            print('Encoded Message: {}'.format(encoding(letter, shift)))

        elif choice == 'd':
            letter = input('Enter string to encode:\n')
            shift = int(input('Enter amount to shift:\n'))
            print('Original Message: {}'.format(letter))
            print('Decoded Message: {}'.format(decoding(letter, shift)))
    else:
        print('That is not a valid response, try again')

else:
    print('Thank You!')