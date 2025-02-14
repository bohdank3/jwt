import jwt
import time
import uuid

APPLICATION_ID = "e077305b"
PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCx0RTzn7Vd0vIW
Qw2XSfnJZvNePJvfcHTUTQBO+nzqQpCP/wElOoSIMGiEn6SFWt6rHSnP2Skef9Z1
wtFKFmKAEZ0EElkjcAPsusi7lhDNzMJdbZTxD/JhEe1+Ou+X20pEMR7SN/3uL8l/
h7aQ1HvwVYYAxn3UEwgkeaWjPYSLsuzlDOWQlasrxDpdJWznWdHNzcyBvdab55J/
VjL64rMmv2Z9ykWBHumT2xajENVUjscrNC1uxUc81J+kHNP5xpeV5hoj1oiDiQ4Z
MU0kh2tRvMNy/QlfKXLJO1TaAuxOq4cPAp7p6a0JHXx//tfrCiFYS2qrbDd2oor+
642HUyoJAgMBAAECggEACBe92xHZBWJwR47l442BQE2esU3GqR/4BgeHhl13g1cX
N26BxPBJj6pmv1tF3hasjRLtNof2i2xPCU03pqZBKMn+Bu1QDQ3wJ8ofQ6ZVsNm3
70LPy6IQENa2vXV9adn+b2V66ewuP7TOEcjn7rLoMLmu7E8cWYmqNIEsbP/Qp5js
xuMKJhzmXVCqpnhCrNFLJFc6jrgNEJNfLf/xvJsaoxTEGfCnSCvFTA2mIw8RkmjS
NmV86UKW+z9kqrKnvIbcbTkHmiZGhNHrcGbDIbeWB/p2EDbC+4kChLqtbYclQt8u
wwUWe+gukLavDkhYW7bqqQ+qTKTuuvbk42Whv1WNuQKBgQD11GktpuPZO2N06TFK
9whx+7US++TMHJUeCyA5B76wdtAkNB59+MXmB4o4CzYN/mGCvVQCPGXSBmh1gTYW
yaHYhlEdOo0c6fIEBCdGzyTh6X0ymr3a35ly9jlN5AmSHru7sgGtoiwsT0cx4hjm
xR470AYSyj7zrB5eRCjzQNdFLQKBgQC5LFft0S2I7qIOJXiqLQSwsZiOt1gg2nOQ
DNiF/dBvkf0lv9WtzJgF7GnzCWwOuv/5TV0mtmBux+UhNgE7M+LIX+dhhV4QkiU3
qezkS7pKwXETmP9v8U+1loieQiqEAoefKVkUSA1Z7GCL2WK9yr1apZrSsvSezbuW
6sMfVEj5zQKBgBAzWmcey39CcbB/ubbmBtF0NB+3KAHnlFAxjYMUppV8jwUDxkqo
/WnGb254Fqzfac+y6HlpP5CSyYmM5WKlERxy5Z+Wfzw7kq5/E5OQDS8yMwUFu6NT
/wnbfjVK5PKTQe4BsiieOmkFJHz+GIQE05Q/hlbwqytl2W5+8W/ugwFVAoGASerS
msNCawPfOshod34K/kGWhXnYuxyYvurxz+L2vmLHa7c9I+ik0tCBppufP+4T2j+w
rJBmxDIVXAGD0k8u+w+VfI9Rckn0g1jYkHVOQyMe8VTEurnYOMODe7Er6ZBc9QL7
ZSYx9jBuhcTcLqjsl2+98teu4Gl9tYu3Ih1yGA0CgYEA8Apxh417szg7pqfc9dD7
56z5ia4oskCjCnAJfw/Vt+mb/H+kG9t4gUKocHfWTdKj0KKU8r8IZZuMMoZQmM9E
K0VZmh/P/M4B89DUCLSso5cdO9TPJb+sArRasKIEeVpir+QVc2qMELHMKtjM1OEc
9/QGmPT0FadG8Fk7yJgGxI4=
-----END PRIVATE KEY-----"""

def generate_token():
    iat = int(time.time())
    exp = iat + 900  
    jti = str(uuid.uuid4())
    
    payload = {
        "application_id": APPLICATION_ID,
        "iat": iat,
        "exp": exp,
        "jti": jti
    }
    
    token = jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token

def handle(data):
    data["jwt_token"] = generate_token()
    return data
