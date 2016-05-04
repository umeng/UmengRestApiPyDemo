# UmengRestApiPyDemo


# 调用方法  
aes_key = '这里放App_Secret'  
data = prpcrypt(aes_key).encrypt(data)  
data = base64.b64encode( data )  
print data
 
