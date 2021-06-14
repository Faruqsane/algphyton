"""
Bastion Faruq Sane/20083000075/2C
Soal No. 8 alpikasi 6a
Perhitungan Nilai Total Transaksi Pembelian Printer

"""
ulang="y"
while ulang=="y" or ulang =="Y":
#Siapkan variabel
    print("===========================")
    print(" APLIKASI 6a")
    print(" Pembelian printer")
    print("===========================")
    u=1
    #Hitung
    u =input(" Masukkan Banyak Printer = ")
    n=int(u)
    harga = n * 660000
    print(" Total Harga Pembelian Printer= Rp.",harga)
    ulang = input("\n Ulang program? y/t = ")
    if ulang=="t" or ulang=="T":
        break