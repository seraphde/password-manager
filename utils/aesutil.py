

import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import sys

def encrypt(key, source, encode=True, keyType = 'hex'):
	'''
	Parameters:
	key - The key with which you want to encrypt. You can give a key in hex representation (which will then be converted to bytes) or just a normal ascii string. Default is hex
	source - the message to encrypt
	encode - whether to encode the output in base64. Default is true
	keyType - specify the type of key passed

	Returns:
	Base64 encoded cipher
	'''

	source = source.encode()
	if keyType == "hex":
		 
		key = bytes(bytearray.fromhex(key))
	

	IV = Random.new().read(AES.block_size) 
	encryptor = AES.new(key, AES.MODE_CBC, IV)
	padding = AES.block_size - len(source) % AES.block_size  
	source += bytes([padding]) * padding 
	data = IV + encryptor.encrypt(source)  
	return base64.b64encode(data).decode() if encode else data


def decrypt(key, source, decode=True,keyType="hex"):
	'''
	Parameters:
	key - key to decrypt with. It can either be an ascii string or a string in hex representation. Default is hex representation
	source - the cipher (or encrypted message) to decrypt
	decode - whether to first base64 decode the cipher before trying to decrypt with the key. Default is true
	keyType - specify the type of key passed

	Returns:
	The decrypted data
	'''

	source = source.encode()
	if decode:
		source = base64.b64decode(source)

	if keyType == "hex":
		
		key = bytes(bytearray.fromhex(key))
	
	IV = source[:AES.block_size]  
	decryptor = AES.new(key, AES.MODE_CBC, IV)
	data = decryptor.decrypt(source[AES.block_size:]) 
	padding = data[-1] 
	if data[-padding:] != bytes([padding]) * padding:  
		raise ValueError("Invalid padding...")
	return data[:-padding]  
