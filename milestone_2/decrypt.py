def decrypt_message(encrypted_message, key):
    decrypted_message = ""

    for char in encrypted_message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                new_char = chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
            else:
                new_char = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            decrypted_message += new_char
        else:
            decrypted_message += char

    return decrypted_message


encrypted_message = input("Enter the encrypted message: ").strip()
key = int(input("Enter the decryption key (the same number used for encryption): "))

result = decrypt_message(encrypted_message, key)
print("Decrypted message:", result)
