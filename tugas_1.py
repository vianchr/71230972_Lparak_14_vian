'''
contoh= Anda diminta untuk mencari seluruh teks yang berupa tanggal dengan format
YYYY-MM-DD dan kemudian seluruh tanggal tersebut diambil dan ditampilkan 
kembali dalam format DD-MM-YYYY ditambah dengan perhitungan selisih dengan
tanggal sekarang dalam hari
'''
import re
import datetime
def cari_tanggal(isi):
    x=re.findall("\d\d\d\d-\d\d-\d\d",isi)
    saat_ini=datetime.datetime.now()

    for i in x:
        i=i.split('-')
        Tahun, Bulan, Hari = i
        tanggal=datetime.datetime(int(Tahun), int(Bulan), int(Hari))
        selisih = (saat_ini-tanggal).days
        print(f" {tanggal} {selisih} hari")
    
        
cari_tanggal("Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02).")