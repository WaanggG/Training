
from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrpt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        # new_letter = alphabet[new_position]
        cipher_text += alphabet[new_position]
    print("The encoded text is {cipher_text}")

encrypt(plain_text = text, shift_amount = shift)

def encrypt(cipher_text, shift_amount):
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
