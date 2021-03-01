import requests, datetime, OpenSSL
resp = requests.get('http://uc2.srmfc.ru/crl/srmfc_gost12_2019.crl')
crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1, resp.content)
crl_crypto = crl.get_issuer()
cryptography = crl.to_cryptography()
offset = datetime.timedelta(hours=5)
for type, data in crl_crypto.get_components():
    print(type.decode("utf-8"), data.decode("utf-8"))
print(datetime.datetime.strptime(str(cryptography.last_update), '%Y-%m-%d %H:%M:%S')+datetime.timedelta(hours=5))
print(datetime.datetime.strptime(str(cryptography.next_update), '%Y-%m-%d %H:%M:%S')+datetime.timedelta(hours=5))

