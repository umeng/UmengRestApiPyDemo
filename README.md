# UmengRestApiPyDemo


    data = '{"source_uid": "123312", "source": "qq", "source_name": "hello"}'
    data = json.dumps({"source_uid" : "0", "source" : "self_account"}) # JSON 格式字符串
    data = struct.pack(">I",len(data)) + data
    aes_key = '这里放App_Secret'
    data = prpcrypt(aes_key).encrypt(data)
    data = base64.b64encode( data )
    print data
 
