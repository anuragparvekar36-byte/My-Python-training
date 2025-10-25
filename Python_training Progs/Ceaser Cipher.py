#Ceaser Cipher

def ceaser_encrypt(org_text, shift_amount):
    print("Encryption in progress...")
    cipher_text = ""
    for char in org_text:
        if char in list_alpha:
            position = list_alpha.index(char)
            new_position = (position + shift_amount) % 26
            cipher_text += list_alpha[new_position]
        else:
            cipher_text += char
    print(f"The encoded text is: {cipher_text}")


print("Welcome to Ceaser Cipher Program")

print("Type 'encode' to encrypt, type 'decode' to decrypt:")
direction = input()

print("Type your message:")
text = input().lower()

print("Type the shift number:")
shift = int(input())

list_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if direction == "encode":
    ceaser_encrypt(org_text=text, shift_amount=shift)
elif direction == "decode":
    ceaser_encrypt(org_text=text, shift_amount=-shift)
