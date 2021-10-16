import yagmail #import module Yagmail utk mengirim email
import getpass #import module utk secure password

#variabel input bagian email dan menambahkan attachment 
msg_user = str(input('Masukkan email Anda : '))
msg_password = getpass.getpass("Masukkan Password Email Anda : ")
msg_subject = str(input('Masukkan Subject Email : '))
msg_body = str(input('Masukkan isi pesan email : '))
msg_att = r'C:\Users\syadi\Documents\ai mentorship basic python\foto.jpg'

#membuat file handling untuk membaca receiver_list.txt sebagai penerima email
with open("receiver_list.txt", "r") as file_x:
    penerima = file_x.read().splitlines()

try:
    #initializing the server connection
    yag = yagmail.SMTP(user=msg_user, password=msg_password)
    #sending the email
    yag.send(to= penerima,  subject=msg_subject, contents=msg_body, attachments= msg_att)
    print("\nEmail anda berhasil terkirim!")
except Exception as exception:
    print("Error: %s!\n\n" % exception)