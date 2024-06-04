contoh_email= '''
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
'''
import random
import string
import re
huruf_besar = string.ascii_uppercase
huruf_kecil = string.ascii_lowercase
digit = string.digits
daftar_pass = huruf_besar+ digit+huruf_kecil
panjang_sandi= 8


daftar_email= re.findall(r"(\S+@\S+)", contoh_email)
for email in daftar_email:
    sandi = ''
    for i in range(panjang_sandi):
        sandi += ''.join(random.choices(daftar_pass))
    user = email.split("@")[0]
    print (f"{email} username: {user}, password: {sandi}")

# anton@mail.com username: anton , password: 8u78A2UD

