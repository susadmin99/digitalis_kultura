from Crypto.Cipher import AES
import base64

key = "HWID"  # the key used for encryption
ciphertext = "yPhC...wJtI="  # the ciphertext to decrypt

# initialize the cipher with the key and mode
cipher = AES.new(key.encode("hex"), AES.MODE_CBC)

# decode the base64-encoded ciphertext and decrypt the data
ciphertext_bytes = base64.b64decode(ciphertext)
plaintext_bytes = cipher.decrypt(ciphertext_bytes)

# convert the decrypted bytes to a string and remove padding
plaintext = plaintext_bytes.decode("utf-8").rstrip("\0")

print(plaintext)  # prints the decrypted plaintext
