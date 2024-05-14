def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            elif char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
            elif char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Do you want to encrypt or decrypt?: ").lower()
    if choice == 'encrypt':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'decrypt':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
