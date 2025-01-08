#Building a Caesar Cipher encryption technology

#text=input("Enter a plaintext: ")
#shift=3
#encrypted_text=''
#shift=int(input("Enter a numeric shift for coding:"))

def caesar(text, shift):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    encrypted_text=''
    for char in text.lower():   #to handle upper or lower case situation.
        if char==' ':           # to handle space in the text
            encrypted_text+=char
        else:
            index=alphabet.find(char)
            new_index=index+shift
            encrypted_text+=alphabet[new_index%len(alphabet)]
            print(char, index, new_index)

    print("plaintext: ", text)
    print("ciphertext: ", encrypted_text)

caesar('shahadat hussain', 3)