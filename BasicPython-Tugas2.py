listnama = []
listtelp = []

pilih = True 
while pilih == True:
    print("--- Menu --- ")
    print("1. Daftar Kontak ")
    print("2. Tambah Kontak ")
    print("3. Keluar ")
    pilihan = int(input('pilih menu 1/2/3 ? '))
    if pilihan == 1:
        print("Daftar Kontak: ")
        print("Nama: ",*listnama)
        print("No Telepon: ",*listtelp)
    elif pilihan == 2:
        nama = input("Nama: ")
        listnama.append(nama)
        telp = input("No Telepon: ")
        listtelp.append(telp)
        print("Kontak berhasil ditambahkan")
    elif pilihan == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia ")
#    pilih = input('pilih lanjut/berhenti? ')
#    if pilih == 'berhenti':
#        print('looping berhenti')
#        break
