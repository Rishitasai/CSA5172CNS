import numpy as np


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def matrix_inverse(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det, modulus)
    if det_inv is None:
        raise ValueError("Matrix is not invertible.")
    adjugate = (det_inv * np.round(det * np.linalg.inv(matrix))).astype(int)
    inverse = np.mod(adjugate, modulus)
    return inverse


def hill_decrypt(ciphertext, key):
    key_matrix = np.array(key)
    plaintext = ""
    key_size = key_matrix.shape[0]
    mod = 26  # Assuming the Hill cipher uses the English alphabet

    if gcd(int(round(np.linalg.det(key_matrix))), mod) != 1:
        raise ValueError("Key matrix is not invertible.")

    inverse_key = matrix_inverse(key_matrix, mod)

    for i in range(0, len(ciphertext), key_size):
        block = [ord(c) - ord('a') for c in ciphertext[i:i + key_size]]
        decrypted_block = np.dot(inverse_key, block) % mod
        decrypted_block = [chr(num + ord('a')) for num in decrypted_block]
        plaintext += "".join(decrypted_block)

    return plaintext


def known_plaintext_attack(plaintexts, ciphertexts):
    key_size = len(plaintexts[0])
    plaintext_matrix = np.zeros((len(plaintexts), key_size), dtype=int)
    ciphertext_matrix = np.zeros((len(ciphertexts), key_size), dtype=int)

    for i, plaintext in enumerate(plaintexts):
        plaintext_matrix[i] = [ord(c) - ord('a') for c in plaintext]

    for i, ciphertext in enumerate(ciphertexts):
        ciphertext_matrix[i] = [ord(c) - ord('a') for c in ciphertext]

    key_matrix = np.mod(np.dot(np.linalg.inv(plaintext_matrix), ciphertext_matrix), 26)
    key_matrix = key_matrix.round().astype(int).tolist()

    return key_matrix


# Example usage
plaintexts = ["hello", "world"]
ciphertexts = ["jqnnl", "wtqoi"]

# Perform known plaintext attack
key = known_plaintext_attack(plaintexts, ciphertexts)

print("Recovered key matrix:")
for row in key:
    print(row)

# Decrypt ciphertext using the recovered key
ciphertext = "jxwyz"
recovered_plaintext = hill_decrypt(ciphertext, key)

print("Recovered plaintext:", recovered_plaintext)
