from logo import *
print(logo)              # GUI
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(cipher_decision, plain_text, shift_amt):
    encoded_text = ""
    if cipher_decision == 'decode':
        shift_amt *= -1                          # So that Shift can be -ve as it is in a Decrypter
    else:
        shift_amt *= 1
    for letter in plain_text:
        if letter in letters:                    # If user enters character apart from alphabets
            position = letters.index(letter)
            new_position = position + shift_amt
            encoded_text += letters[new_position]
        else:
            encoded_text += letter
    print(f"The {cipher_decision} text is: {encoded_text}")
    end = input("Do you want to exit the program?: ")
    if end == 'y' or 'Y':
        exit()
    else:
        exit()


def main():
    decision = input("Type 'encode' or 'decode' to decrypt: ")
    text = input("Enter message: ").lower()
    shift = int(input("Enter the value to shift the numbers by: "))
    shift %= 26                                                             # If user enters >45 in shift
    cipher(cipher_decision=decision, plain_text=text, shift_amt=shift)


main()
