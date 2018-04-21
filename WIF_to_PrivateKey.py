#WIF to Private Key
import base58
import binascii

WIF_key_static = input("Enter Your WIF Key : ");

#Decoding base58
decoding = base58.b58decode(WIF_key_static)

#Returning the hex
hex = binascii.hexlify(decoding)

#decoding utf-8
decoded = hex.decode('utf-8')

#dropping the first byte (0x80)
privateKey = decoded[2:-8]

#to uppercase
print(privateKey.upper())


print ("Your Private Key : " + privateKey)
