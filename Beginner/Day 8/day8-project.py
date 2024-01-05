import string

alphabet = string.ascii_lowercase


def ceaser(text, shift_number, direction):
    completed_text = []
    type = ""
    for i, char in enumerate(text):
        type = "encrypted"
        if direction == "e":
            if char in alphabet:
                if alphabet.index(char) + shift_number < len(alphabet):
                    completed_text.append(alphabet[alphabet.index(char) + shift_number])
                else:
                    completed_text.append(alphabet[(alphabet.index(char) + shift_number) - 26])
        else:
            type = "decrypted"
            if char in alphabet:
                if alphabet.index(char) - shift_number >= 0:
                    completed_text.append(alphabet[alphabet.index(char) - shift_number])
                else:
                    completed_text.append(alphabet[26 - (abs(alphabet.index(char) - shift_number))])

    print(f"The {type} message is: {''.join(completed_text)}")


# def decrypt(text, shift_number, direction):
#    plain_text = []
#    for i, char in enumerate(text):
#        if char in alphabet:
#            if alphabet.index(char) - shift_number >= 0:
#                plain_text.append(alphabet[alphabet.index(char) - shift_number])
#            else:
#                plain_text.append(alphabet[26 - (abs(alphabet.index(char) - shift_number))])
#    print(f"The decrypted message is: {''.join(plain_text)}")

done = False

while not done:
    print("Welcome to Ceaser Cipher")
    user_choice = input("Type 'e' to encrypt, or 'd' to decrypt: ")
    user_message = input("Type your message: ")
    user_shift = int(input("Type the shift number to use: "))
    ceaser(text=user_message, shift_number=user_shift, direction=user_choice)
    temp = input("\n\nWould you like decode/encode another message? 'Y' | 'N' ").lower()
    if temp == "n".lower():
        done = True
