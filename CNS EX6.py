def find_inverse(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i
    return None

def decrypt(ciphertext, a, b):
    inverse_a = find_inverse(a)
    if inverse_a is None:
        print("The multiplicative key has no inverse.")
        return ""

    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            c_index = ord(c) - ord('A')
            p_index = (inverse_a * (c_index - b)) % 26
            plaintext += chr(p_index + ord('A'))
        else:
            plaintext += c

    return plaintext


ciphertext = "BUABABUBA"
a = 5  
b = 1
plaintext = decrypt(ciphertext, a, b)
print("Decrypted plaintext:", plaintext)
