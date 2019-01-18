plaintext = input('Enter plain message: ')
ciphertext = ''

for letter in plaintext:
    if letter.isalpha():
        num = ord(letter)
        num += 4
        if (letter.isupper()) and num > ord('Z'):
            num -= 26
        elif (letter.islower()) and num > ord('z'):
            num -= 26
        ciphertext += chr(num)
    else:
        ciphertext += letter

print(ciphertext)
