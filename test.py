import requests
import OpenSSL
resp = requests.get('http://ca.taxnet.ru/ra/cdp/269bd73c83e5b0e56cb475873e55a95cb5bb5c87.crl')
crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1, resp.content)
crl_crypto = crl.get_issuer()
cryptography = crl.to_cryptography()
for type, data in crl_crypto.get_components():
    print(type.decode("utf-8"), data.decode("utf-8"))
print(crl_crypto())
print(cryptography.last_update)
print(cryptography.next_update)

