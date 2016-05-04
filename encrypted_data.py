# -*- coding: utf-8 -*-
import json
import struct
import base64
from Crypto.Cipher import AES



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


if __name__ == '__main__':
    # data = '{"source_uid": "123312", "source": "qq", "source_name": "hello"}'
    data = json.dumps({"source_uid" : "0", "source" : "self_account"}) # JSON 格式字符串
    data = struct.pack(">I",len(data)) + data
    aes_key = '这里放App_Secret'
    data = prpcrypt(aes_key).encrypt(data)
    data = base64.b64encode( data )
    print data
