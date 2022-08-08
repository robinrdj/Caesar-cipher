# Caesar Cipher
import logo


# creating functions
# Encryption
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letters in plain_text:
        if letters not in plain_text:
            cipher_text += letters
        else:
            position = alphabet.index(letters)
            new_position = position + shift_amount

            cipher_text += alphabet[new_position]
    print(f"cipher Text: {cipher_text}")


# Decryption
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letters in cipher_text:
        if letters not in cipher_text:
            plain_text += letters
        else:
            position = alphabet.index(letters)
            new_position = position - shift_amount
            plain_text += alphabet[new_position]
    print(f"plain Text: {plain_text}")


print(logo.logo)
should_continue = True

while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Enter whether u want to 'encrypt' or 'decrypt' the code\n").lower()
    text = input("enter the text \n")
    shift = int(input("Enter the shift amount\n"))
    if shift > 26:
        shift %= 26
    if direction == "encrypt":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decrypt":
        decrypt(cipher_text=text, shift_amount=shift)
    result = input("Do u want to continue. enter 'yes' if u want to and 'no' if u dont want to")
    if result == "no":
        should_continue = false
        print("Goodbye")
