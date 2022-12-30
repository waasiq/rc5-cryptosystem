import streamlit as st
import rc5 
import keysched

plaintext = st.text_input('Please enter the cipher string text to be Encrypt: ')
key = st.text_input('Please enter the string key: ')
rounds = st.number_input('Please enter the number of rounds: ',
                            min_value = 0,
                            max_value = 255,
                            format='%d',
                        )

cipher_text = st.text_input('Please enter the cipher string text to be Decrypt: ')



encrypt = st.button('Encrypt', key='encrypt', help='Encrypt the cipher text', type='primary')
decrypt = st.button('Decrypt', key='decrypt', help='Decrypt the cipher text')


if encrypt:
    key = keysched.rc5_key_schedule(key, rounds)
    xx = rc5.encrypt(plaintext, key, rounds)
    st.write(xx)

if decrypt:
    key = keysched.rc5_key_schedule(key, rounds)
    cipher_text = rc5.decrypt(cipher_text, key, rounds)
    st.write(cipher_text)



