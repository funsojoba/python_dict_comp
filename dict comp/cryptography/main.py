
cipher_result = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(message, key):
    cipher_result.clear()
    for i in message:
        position = alphabet.index(i)
        new_position = (position + key) % len(alphabet)
        cipher_result.append(alphabet[new_position])
        encrypted_message = "".join(cipher_result)

    print(f"Your message encryption: {encrypted_message}")


def decrypt(message, key):
    cipher_result.clear()
    for i in message:
        position = alphabet.index(i)
        new_position = (position - key) % len(alphabet)
        cipher_result.append(alphabet[new_position])
        encrypted_message = "".join(cipher_result)

    print(f"Your message encryption: {encrypted_message}")


while True:
    encr_decr = (input("Do you want to encrypt 'E' or decrypt 'D': ")).lower()
    if encr_decr == 'e':
        message = (input("Please enter your message to encrypt:").lower())
        if len(message.split()) == 0:
            print("Enter something nah")
        try:
            key = int(input("Please input your encryption key: "))
        except ValueError:
            print("Your key must be a number")
        else:
            encrypt(message, key)
    elif encr_decr == 'd':
        message = (input("Please enter your message to decrypt:").lower())
        try:
            key = int(input("Please input your decryption key: "))
        except ValueError:
            print("Your value should be a number")
        else:
            decrypt(message, key)
    else:
        print("Please enter 'E' to encrypt message and 'D' to decrypt message")
        continue
    decision = (input("Do you want to do it again 'Y' or 'N': ")).lower()
    if decision == 'y':
        continue
    else:
        print("Thank you for using our service, have a wonderful day")
        break


# def check_number():
#   collected_number = int(input("Please input number: "))

#   try:
#     numb_sqare = collected_number **2
#     print(numb_sqare)
#   except Exception:
#     print("Please input number")
#     check_number()

# check_number()
