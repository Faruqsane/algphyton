"""

Bastion Faruq Sane/20083000075/2C
Soal No. 7 aplikasi 5b
Program Cek Tingkat Usia

"""
ulang="y"
while ulang=="y" or ulang =="Y":
#Siapkan variabel
    print("===========================")
    print(" APLIKASI 5b")
    print(" CEK Tingkat Usia")
    print("===========================")
    n=1
    
    #Cek batasan usia 0-100
    while n>0 and n<=100:
        u = input("Masukan Usia = ")
        n = int(u)
        if n>0 and n<=100:
            if n>=60:
                    sts= "Lansia"
            elif n>=35:
                    sts= "Dewasa"
            elif n>=18:
                    sts="Pemuda"
            elif n>=15:
                    sts="Remaja"
            else: sts="Anak"
            print(sts)

            ulang=input("Ingin Mengecek Kembali? y/t = ")
            if ulang=="t" or ulang =="T":
                break

        else:
            pesan="Masukan Kembali Angka Usia Antara 0-100"
            print(pesan)
            print()
