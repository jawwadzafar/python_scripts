import hashlib
import base58
import binascii

private_key_static = input("Enter Your Private Key : ");

extended_key = "80"+private_key_static
first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()

# add checksum to end of extended key
final_key = extended_key+second_sha256[:8]

# Wallet Import Format = base 58 encoded final_key
WIF = base58.b58encode(binascii.unhexlify(final_key))

print ("Your WIF Key : " + WIF)
