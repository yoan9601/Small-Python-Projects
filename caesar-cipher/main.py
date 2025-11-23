# Caesar Cipher
# Classic encryption/decryption tool with restart feature
# Author: yoan9601

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    result = ""
    shift = shift % 26  # защита срещу големи числа
    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            result += alphabet[new_position]
        else:
            result += char  # запазва символи, числа, интервали
    print(f"\nThe {direction}d text is: {result}\n")

print("Welcome to the Caesar Cipher!")
print("=" * 50)

while True:
    while True:
        direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
        if direction in ["encode", "decode"]:
            break
        print("Please type 'encode' or 'decode'.")

    text = input("Type your message:\n").lower()
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("Please enter a valid number!")

    caesar(text=text, shift=shift, direction=direction)

    while True:
        restart = input("Do you want to go again? (yes/no): \n").lower()
        if restart in ["yes", "no"]:
            break
        print("Please type 'yes' or 'no'.")

    if restart == "no":
        print("\nThank you for using Caesar Cipher! Goodbye!\n")
        break
