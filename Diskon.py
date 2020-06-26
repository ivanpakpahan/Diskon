import os
import time
v=1
while v<=10:
        print("Yo kozo...lagi loading ",v,"%")
        time.sleep(1)        
        os.system('cls')
        v=v+1
print("Yo kozo...lagi loading 10000000%")
time.sleep(2)
os.system('cls')
while True:
    os.system('cls')
    print(" \t \t \t |-------- PROGRAM DISKON --------|")
    print(" \t \t \t |-------------- IP --------------|")
    print(" \t \t \t |--------------------------------|")
    i = 1
    f = 0
    g = []
    strNama=""
    print("\n")
    print("\n")
    print("Jangan salah input kozo, angka dan huruf beda bisa error")
    print("\n")
    print("\n")
    b= int(input("Masukkan jumlah pembelian       : "))
    while i<=b:
        print("-----------------------------------------------------------|")
        print("Barang ke -",i)
        c = input("Masukkan nama barang            : ")
        d = int(input("Masukkan harga barang /1 unit Rp: "))
        e = int(input("Masukkan jumlah unit            : "))
        print("-----------------------------------------------------------|")
        strNama = strNama +"- "+ c + "\n"
        f = (d*e)
        g.append(f)
        i=i+1
    h = sum(g)
    print("Subtotal Rp: ","[",h,"]")
    print("List barang : \n"+strNama)
    jawab = None
    while jawab not in ("ya", "tidak"):
        jawab = input("Apakah anda seorang member? (ya/tidak): ")
        if jawab == "ya":
            print("Member akan mendapatkan 3 poin setiap pembelian 7700 Rupiah")
            j = h//7700
            k = j*3
            print("Anda mendapatkan poin sebanyak : ",k)
            jwb = None
            while jwb not in ("ya", "tidak"):
                jwb = input("1 poin senilai Rp 500, apakah anda ingin menukarnya? (ya/tidak) : ")
                if jwb == "ya":
                    Total = h-(k*500)
                    print("Jumlah yang harus dibayar : Rp",Total)
                elif jwb == "tidak":
                    Total = h
                    print("Jumlah yang harus dibayar : Rp",Total)
                else:
                    print("Masukkan pilihan anda")
        elif jawab == "tidak":
            Total = h
            print("Jumlah yang harus dibayar : Rp",Total)
        else:
            print("Masukkan pilihan anda.")
    while True:
        print("------------------------------------------------------------")
        jwb2 = None
        jwb2 = input('Ulangi perhitungan? (ya/tidak): ')
        print("------------------------------------------------------------")
        if jwb2 in ('ya', 'tidak'):
            break
        print ('Masukkan pilihan anda.')
    if jwb2 == 'ya':
        os.system('cls')
        continue
    else:
        print('Terimakasih')
        break


