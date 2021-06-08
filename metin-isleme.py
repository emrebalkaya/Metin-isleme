import locale
locale.setlocale(locale.LC_ALL,("tr","UTF-8"))
devam="e"
metin_toplam = ""
while devam in"eE":
    metin = input("Metni giriniz: ")
    metin_toplam +=" " + metin
    kelimeler = metin.split(" ")
    satır_genisligi = int(input("İstediğiniz satır genişliğini giriniz: "))
    while satır_genisligi != 0:
        yeni_metin = "\n"
        sayac = 0
        satırlar = []
        satır_sayısı = 1
        en_uzun_kelimenin_uzunlugu=0
        while True:
            satır_kelimeleri=[]
            a = len(kelimeler[sayac])+1
            if a -1 == satır_genisligi:
                a -= 1
            kelime_uzunlugu = len(kelimeler[sayac])
            satır_kelimeleri.append(kelimeler[sayac])
            while a <= satır_genisligi:
                a += len(kelimeler[sayac+1])+1
                kelime_uzunlugu += len(kelimeler[sayac+1])
                satır_kelimeleri.append(kelimeler[sayac+1])
                sayac +=1
                if a-1 == satır_genisligi:
                    a = satır_genisligi
                if sayac == len(kelimeler)-1:
                    break
            kelime_uzunlugu -= len(kelimeler[sayac])
            satır_kelimeleri.pop()
            bosluk_uzunlugu = satır_genisligi-kelime_uzunlugu
            bosluk_yeri = len(satır_kelimeleri)-1
            if satır_sayısı % 2 == 1:
                if bosluk_yeri != 0 and bosluk_uzunlugu % bosluk_yeri == 0:
                    bosluk_sayısı = bosluk_uzunlugu // bosluk_yeri
                    for kelime in satır_kelimeleri:
                        yeni_metin += kelime
                        yeni_metin += " "*bosluk_sayısı
                    yeni_metin = yeni_metin[:(satır_genisligi+1)*satır_sayısı]
                elif bosluk_yeri != 0 and bosluk_uzunlugu % bosluk_yeri != 0:
                    bosluk_sayısı = bosluk_uzunlugu // bosluk_yeri
                    bosluk_sayacı = 0
                    while bosluk_uzunlugu % bosluk_yeri != 0:
                        yeni_metin += satır_kelimeleri[bosluk_sayacı]
                        yeni_metin += " " * bosluk_sayısı + " "
                        bosluk_uzunlugu -= (bosluk_sayısı + 1)
                        bosluk_sayacı += 1
                        bosluk_yeri-=1
                    for i in range(len(satır_kelimeleri[bosluk_sayacı:])):
                        yeni_metin += satır_kelimeleri[bosluk_sayacı]
                        bosluk_sayacı += 1
                        yeni_metin += " "*bosluk_sayısı
                    yeni_metin = yeni_metin[:(satır_genisligi+1)*satır_sayısı]
                else:
                   yeni_metin+=satır_kelimeleri[0]+" "*bosluk_uzunlugu
            else:
                if bosluk_yeri != 0 and bosluk_uzunlugu % bosluk_yeri == 0:
                    bosluk_sayısı = bosluk_uzunlugu // bosluk_yeri
                    for kelime in satır_kelimeleri:
                        yeni_metin += kelime
                        yeni_metin += " "*bosluk_sayısı
                    yeni_metin = yeni_metin[:(satır_genisligi+1)*satır_sayısı]
                elif bosluk_yeri != 0 and bosluk_uzunlugu % bosluk_yeri != 0:
                    bosluk_sayısı = bosluk_uzunlugu // bosluk_yeri
                    bosluk_sayacı = 0
                    while bosluk_uzunlugu % bosluk_yeri != 0:
                        yeni_metin += satır_kelimeleri[bosluk_sayacı]
                        yeni_metin += " " * bosluk_sayısı
                        bosluk_uzunlugu -= bosluk_sayısı
                        bosluk_sayacı += 1
                        bosluk_yeri-=1
                    for i in range(len(satır_kelimeleri[bosluk_sayacı:])):
                        yeni_metin += satır_kelimeleri[bosluk_sayacı]
                        bosluk_sayacı += 1
                        yeni_metin += " "*bosluk_sayısı+" "
                    yeni_metin = yeni_metin[:(satır_genisligi+1)*satır_sayısı]
                else:
                    yeni_metin+=satır_kelimeleri[0]+" "*bosluk_uzunlugu
            satırlar.append(satır_kelimeleri)
            yeni_metin += "\n"
            satır_sayısı += 1
            if sayac == len(kelimeler)-1:
                break
        yeni_metin=yeni_metin[:(satır_genisligi+1)*(satır_sayısı-2)+1]

        for i in range(len(satırlar[satır_sayısı-2])):
            yeni_metin+=satırlar[satır_sayısı-2][i]
            yeni_metin+=" "
        for i in kelimeler:
            b=len(i)
            if b>en_uzun_kelimenin_uzunlugu:
                en_uzun_kelimenin_uzunlugu=b
        if en_uzun_kelimenin_uzunlugu>= satır_genisligi+1:
            yeni_metin+="\n"
        yeni_metin+=str(kelimeler[-1])
        print(yeni_metin)
        satır_genisligi = int(input("İstediğiniz satır genişliğini giriniz (çıkış için 0 giriniz): "))
    kelime_listesi = []
    kelime_tekrar_keys=[]
    kelimeler = metin.split(" ")
    for i in range(len(kelimeler)):
        kelimeler[i] = kelimeler[i].replace("i","\u0130")
        kelimeler[i] = kelimeler[i].upper()
    kelime_tekrar = {}
    for kelime in kelimeler:
        if kelime not in kelime_listesi:
            kelime_listesi.append(kelime)
    kelimeler_sıralı=sorted(kelime_listesi,key=locale.strxfrm)
    for i in range(len(kelimeler_sıralı)):
        kelime_tekrar[kelimeler_sıralı[i]]=kelimeler.count(kelimeler_sıralı[i])
    max_tekrar=max(kelime_tekrar.values())
    while True:
        for key in kelime_tekrar:
            if kelime_tekrar[key]==max_tekrar:
                kelime_tekrar_keys.append(key)
        max_tekrar-=1
        if max_tekrar==0:
            break

    kelime_tekrar_sıralı = reversed(sorted(kelime_tekrar.values()))
    kelime_tekrar_sıralı_liste=[]
    for i in kelime_tekrar_sıralı:
        kelime_tekrar_sıralı_liste.append(i)

    print("Kelime               Tekrar Say      |       Kelime               Tekrar Say")
    print("-------------------- ----------      |       -------------------- ----------")
    for i in range(len(kelime_listesi)):
        print("{:<21}".format(kelimeler_sıralı[i]),"{:<10}".format(kelimeler.count(kelimeler_sıralı[i])),"    |       ",end="")
        print("{:<21}".format(kelime_tekrar_keys[i]),"      ",kelime_tekrar_sıralı_liste[i])
    devam=input("Yeni metin girmek istiyor musunuz (e/E/h/H)?: ")
metin_toplam= metin_toplam[1:]
kelimeler = metin_toplam.split(" ")
kelime_listesi = []
kelime_tekrar_keys=[]
for i in range(len(kelimeler)):
    kelimeler[i] = kelimeler[i].replace("i","\u0130")
    kelimeler[i] = kelimeler[i].upper()
kelime_tekrar = {}
for kelime in kelimeler:
    if kelime not in kelime_listesi:
        kelime_listesi.append(kelime)
kelimeler_sıralı=sorted(kelime_listesi,key=locale.strxfrm)
for i in range(len(kelimeler_sıralı)):
    kelime_tekrar[kelimeler_sıralı[i]]=kelimeler.count(kelimeler_sıralı[i])
max_tekrar=max(kelime_tekrar.values())
while True:
    for key in kelime_tekrar:
        if kelime_tekrar[key]==max_tekrar:
            kelime_tekrar_keys.append(key)
    max_tekrar-=1
    if max_tekrar==0:
        break

kelime_tekrar_sıralı = reversed(sorted(kelime_tekrar.values()))
kelime_tekrar_sıralı_liste=[]
for i in kelime_tekrar_sıralı:
    kelime_tekrar_sıralı_liste.append(i)
print("Kelime               Tekrar Say      |       Kelime               Tekrar Say")
print("-------------------- ----------      |       -------------------- ----------")
for i in range(len(kelime_listesi)):
    print("{:<21}".format(kelimeler_sıralı[i]),"{:<10}".format(kelimeler.count(kelimeler_sıralı[i])),"    |       ",end="")
    print("{:<21}".format(kelime_tekrar_keys[i]),"      ",kelime_tekrar_sıralı_liste[i])
harf_matrisi=[]
alfabe=["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
for i in range(len(alfabe)):
    harf_tekrar=[]
    for j in range(20):
        harf_tekrar.append(0)
    harf_matrisi.append(harf_tekrar)
for i in range(len(kelimeler)):
    for j in range(len(kelimeler[i])):
        for harf in alfabe:
            if kelimeler[i][j] == harf:
                harf_matrisi[alfabe.index(harf)][j] += 1
print("     Kelime İçindeki Konum")
print("Harf  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20 Toplam")
print("---- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ------")
for i in range(len(alfabe)):
    print("{:<6}".format(alfabe[i]),end="")
    for j in range(20):
        print("{:<4}".format(harf_matrisi[i][j]),end="")
    print(sum(harf_matrisi[i]))
harf_uzayı=open("harf_uzayi.txt","r",encoding="utf-8")
harf_matrisi=[]
for line in harf_uzayı:
    lines=[]
    lines.append(line)
    harf_matrisi.append(lines)
harf_uzayı.close()
def uzayda_kelime_ara(kelime,harf_matrisi):
    uzay_listesi=[]
    boşmu=True
    başlangıç = 0
    kelime_uzunluğu = len(kelime)
    bitiş = kelime_uzunluğu
    sayaç = 0
    while True:
        yon=0
        index1 = -1
        if kelime == harf_matrisi[sayaç][0][başlangıç-kelime_uzunluğu:bitiş-kelime_uzunluğu]:
            pass
        else:
            sayaç = 0
        while sayaç != len(harf_matrisi)-1:
            for j in range(len(harf_matrisi)-kelime_uzunluğu+1):
                if kelime == harf_matrisi[sayaç][0][başlangıç:bitiş]:
                    index1=j
                    boşmu=False
                    başlangıç +=kelime_uzunluğu-1
                    bitiş +=kelime_uzunluğu-1
                başlangıç+=1
                bitiş+=1
                if kelime == harf_matrisi[sayaç][0][başlangıç-kelime_uzunluğu:bitiş-kelime_uzunluğu]:
                    break
            sütun_numarası = index1 + 1
            satır_numarası = sayaç+1
            if kelime == harf_matrisi[sayaç][0][başlangıç-kelime_uzunluğu:bitiş-kelime_uzunluğu]:
                break
            başlangıç = 0
            bitiş = kelime_uzunluğu
            sayaç += 1
        if satır_numarası < len(harf_matrisi) // 2 and sütun_numarası > len(harf_matrisi) // 2:
            yon = 2
        elif satır_numarası == len(harf_matrisi) // 2 and sütun_numarası > len(harf_matrisi) // 2:
            yon = 3
        elif satır_numarası > len(harf_matrisi) // 2 and sütun_numarası > len(harf_matrisi) // 2:
            yon = 4
        elif satır_numarası > len(harf_matrisi) // 2 and sütun_numarası + kelime_uzunluğu < len(harf_matrisi) // 2:
            yon = 6
        elif satır_numarası == len(harf_matrisi) // 2 and sütun_numarası + kelime_uzunluğu < len(harf_matrisi) // 2:
            yon = 7
        elif satır_numarası < len(harf_matrisi) // 2 and sütun_numarası + kelime_uzunluğu < len(harf_matrisi) // 2:
            yon = 8
        elif satır_numarası < len(harf_matrisi) // 2:
            yon = 1
        elif satır_numarası > (len(harf_matrisi) // 2):
            yon = 5
        tuple=(satır_numarası,sütun_numarası,yon)
        if index1 == -1:
            tuple=()
            break
        else:
            uzay_listesi.append(tuple)
    if boşmu!=False:
        uzay_listesi=[]
    return uzay_listesi
print("Kelime                    Satır No Sütun No Yönü")
print("------------------------- -------- -------- ---------")
for kelime in kelime_listesi:
    if len(uzayda_kelime_ara(kelime,harf_matrisi))!=0:
        for i in range(len(uzayda_kelime_ara(kelime,harf_matrisi))):
            print("{:<25}".format(kelime),"{:<12}".format(uzayda_kelime_ara(kelime,harf_matrisi)[i][0]),"{:<5}".format(uzayda_kelime_ara(kelime,harf_matrisi)[i][1]),end="")
            if uzayda_kelime_ara(kelime,harf_matrisi)[i][2]==1:
                print("Kuzey")
            elif uzayda_kelime_ara(kelime, harf_matrisi)[i][2] == 2:
                print("Kuzeydoğu")
            elif uzayda_kelime_ara(kelime, harf_matrisi)[i][2] == 3:
                print("Doğu")
            elif uzayda_kelime_ara(kelime, harf_matrisi)[i][2] == 4:
                print("Güneydoğu")
            elif uzayda_kelime_ara(kelime, harf_matrisi)[i][2] == 5:
                print("Güney")
            elif uzayda_kelime_ara(kelime, harf_matrisi)[i][2] == 6:
                print("Güneybatı")
            elif uzayda_kelime_ara(kelime, harf_matrisi)[i][2] == 7:
                print("Batı")
            else:
                print("Kuzeybatı")
    else:
        print("{:<25}".format(kelime),"Bulunamadı!")