import streamlit as st
import rc5
import keysched

def show_documentation():
    st.title("RC5 Encryption and Decryption Documentation")

    st.markdown("## Overview")
    st.write("Welcome to the documentation page for the RC5 encryption and decryption application.")
    st.write("RC5 is a symmetric key block cipher algorithm that operates on fixed-size blocks of data.")
    st.write("This application allows you to encrypt and decrypt text using the RC5 algorithm.")

    st.markdown("## Working of RC5 Algorithm")
    st.write("The RC5 algorithm consists of the following steps:")
    st.write("1. **Key Schedule**: The algorithm generates a key schedule based on the provided encryption key.")
    st.write("2. **Encryption**: The plaintext is divided into blocks of a fixed size. Each block undergoes a series of encryption rounds, where the block is mixed with the subkeys from the key schedule.")
    st.write("3. **Decryption**: The ciphertext is divided into blocks of the same fixed size. Each block undergoes a series of decryption rounds, where the block is mixed with the subkeys in reverse order.")
    st.write("4. The final encrypted or decrypted output is obtained by concatenating the processed blocks.")

    st.markdown("## Encryption")
    st.write("To encrypt text using RC5, follow these steps:")
    st.write("1. Enter the plaintext in the 'Enter the plaintext to encrypt' input box.")
    st.write("2. Enter the encryption key in the 'Enter the encryption key' input box.")
    st.write("3. Specify the number of encryption rounds using the 'Enter the number of encryption rounds' input field.")
    st.write("4. Click the 'Encrypt' button.")
    st.write("5. The encrypted text will be displayed in the 'Encrypted Text' section.")

    st.markdown("## Decryption")
    st.write("To decrypt text using RC5, follow these steps:")
    st.write("1. Enter the ciphertext in the 'Enter the ciphertext to decrypt' input box.")
    st.write("2. Enter the encryption key used for encryption in the 'Enter the encryption key' input box.")
    st.write("3. Specify the number of encryption rounds (should be the same as used during encryption) using the 'Enter the number of encryption rounds' input field.")
    st.write("4. Click the 'Decrypt' button.")
    st.write("5. The decrypted text will be displayed in the 'Decrypted Text' section.")

    st.markdown("## Additional Resources")
    st.write("For more detailed information on the RC5 algorithm, you can refer to the official paper:")
    st.write("[RC5 Encryption Algorithm](https://link.springer.com/content/pdf/10.1007/3-540-60590-8_7.pdf?pdf=inline%20link)")

    st.markdown("## Notes")
    st.write("- Make sure to use the same encryption key and number of rounds during both encryption and decryption.")
    st.write("- The application uses base64 encoding for displaying the encrypted and decrypted text.")
    st.write("- Padding bytes may be added during encryption to ensure the plaintext length is a multiple of the block size.")
    st.write("- The padding bytes are automatically removed during decryption.")

# Sidebar
def render_sidebar():
    st.sidebar.title("Menu")
    selected_page = st.sidebar.radio("Select a page", ("Encryption/Decryption", "Documentation"))

    if selected_page == "Encryption/Decryption":
        show_encryption_decryption()
    elif selected_page == "Documentation":
        show_documentation()

def show_encryption_decryption():
    st.title("RC5 Encryption and Decryption")

    st.subheader("Encryption")
    plaintext = st.text_input("Enter the plaintext to encrypt:")
    key = st.text_input("Enter the encryption key:")
    rounds = st.number_input("Enter the number of encryption rounds:", min_value=0, max_value=255, format="%d")

    encrypt_button = st.button("Encrypt", key="encrypt", help="Encrypt the plaintext", type="primary")

    if encrypt_button:
        key_schedule = keysched.rc5_key_schedule(key, rounds)
        encrypted_text = rc5.encrypt(plaintext, key_schedule, rounds)
        st.markdown(f"**Encrypted Text:**")
        st.write(encrypted_text)

    st.subheader("Decryption")
    cipher_text = st.text_input("Enter the ciphertext to decrypt:")

    decrypt_button = st.button("Decrypt", key="decrypt", help="Decrypt the ciphertext")

    if decrypt_button:
        key_schedule = keysched.rc5_key_schedule(key, rounds)
        decrypted_text = rc5.decrypt(cipher_text, key_schedule, rounds)
        st.markdown(f"**Decrypted Text:**")
        st.write(decrypted_text)

# Main function
def main():
    render_sidebar()

if __name__ == "__main__":
    main()