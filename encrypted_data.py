import struct
import base64
from Crypto.Cipher import AES

# data = '{"source_uid": "123312", "source": "qq", "source_name": "hello"}'
data = '{"source_uid" : "0", "source" : "self_account"}'
data = struct.pack(">I",len(data)) + data

class prpcrypt():
	def __init__(self, key):
		self.key = key
		self.mode = AES.MODE_CBC
		self.iv = self.key[:16]
	def encrypt(self, text):
		cryptor = AES.new(self.key, self.mode, self.iv)
		length = 32
		count = len(text)
		amount = length - (count % length)
		if amount == 0:
			amount = length
		pad_chr = chr(amount & 0xFF)
		new_text = text + (pad_chr * amount)
		ciphertext = cryptor.encrypt(new_text)
		return ciphertext

aes_key = '这里放API_Secret'
data = prpcrypt(aes_key).encrypt(data)
data = base64.b64encode( data )
print data