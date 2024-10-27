def encrypt_message(message, key):
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            else:
                new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            encrypted_message += new_char
        else:
            encrypted_message += char

    return encrypted_message


if __name__ == "__main__":
    user_message = input("Enter your message: ").strip()
    key = int(input("Enter the encryption key (a number): "))

    result = encrypt_message(user_message, key)
    print("Encrypted message:", result)
