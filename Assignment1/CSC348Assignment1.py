def caesar_cipher(message, shift, encrypt = True):
    result = ""

    if not encrypt:
        shift = -shift

    for char in message:
        ascii_value = ord(char)

        if 32 <= ascii_value <= 126:
            shifted = ((ascii_value - 32 + shift) % 95) + 32
            result += chr(shifted)

        else:
            result += char

    return result

def vigenere_cipher(message, keyword, encrypt = True):
    result = ""
    key_length = len(keyword)
    key_index = 0

    for char in message:
        ascii_value = ord(char)
    
        if 32 <= ascii_value <= 126:
            get_shift = keyword[key_index % key_length]
            shift = ord(get_shift) - 32

            result += caesar_cipher(char, shift, encrypt)
            key_index += 1
        else:
         result += char

    return result    


message = "I love WFU (go Deacs!)"
shift = 4
keyword = "CSC"

caesar_encrypted = caesar_cipher(message, shift, encrypt=True)
caesar_decrypted = caesar_cipher(caesar_encrypted, shift, encrypt=False)

vigenere_encrypted = vigenere_cipher(message, keyword, encrypt=True)
vigenere_decrypted = vigenere_cipher(vigenere_encrypted, keyword, encrypt=False)

print ("Encrypted message with Caesar: " + caesar_encrypted)
print ("Decrypted message with Caesar: " + caesar_decrypted)
print ("Encrypted message with Vigenere: " + vigenere_encrypted)
print ("Decrypted message with Vignere: " + vigenere_decrypted)