

#* This py file contains code for coverting text to binary and vice versa
def encrypt(plaintext, S , rounds):
    # Convert the plaintext and key strings to bytes objects
    plaintext_bytes = plaintext.encode()

    # Initialize the encryption variables
    A = B = 0
    ciphertext = b''

    # Encrypt each block of the plaintext
    for i in range(0, len(plaintext_bytes), 8):
        A = int.from_bytes(plaintext_bytes[i:i+4], 'little')
        B = int.from_bytes(plaintext_bytes[i+4:i+8], 'little')

        # Perform the encryption rounds
        for j in range(1, rounds+1):
            A = ((A + S[2*j-1]) & 0xFFFFFFFF) ^ B
            B = ((B + S[2*j]) & 0xFFFFFFFF) ^ A

        # Concatenate the encrypted blocks
        ciphertext += (A.to_bytes(4, 'little') + B.to_bytes(4, 'little'))

    return ciphertext

def decrypt(ciphertext, S , rounds):
    # Initialize the decryption variables
    A = B = 0
    plaintext = b''

    # Decrypt each block of the ciphertext
    for i in range(0, len(ciphertext), 8):
        A = int.from_bytes(ciphertext[i:i+4], 'little')
        B = int.from_bytes(ciphertext[i+4:i+8], 'little')

        # Perform the decryption rounds
        for j in range(rounds, 0, -1):
            B = (B ^ A) - S[2*j] & 0xFFFFFFFF
            A = (A ^ B) - S[2*j-1] & 0xFFFFFFFF

        # Concatenate the decrypted blocks
        plaintext += (A.to_bytes(4, 'little') + B.to_bytes(4, 'little'))

    return plaintext.decode()


