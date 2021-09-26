uteori = float(input('masukkan nilai ujian teori: '))
upraktek = float(input('masukkan nilai ujian praktek: '))
if uteori >= 70.0 and upraktek >= 70.0:
    print("Selamat, anda lulus!")
elif uteori >= 70.0 and upraktek < 70.0:
    print("Anda harus mengulang ujian praktek.")
elif uteori < 70.0 and upraktek >= 70.0:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")