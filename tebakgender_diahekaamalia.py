nama = input("Masukkan nama anda: ") #input nama
nama = nama.split()
def array(nama):
    jumcow=jumcew=0 #inisiasi awal
    for karakter in nama[0]: # mengecek setiap karakter/huruf pada nama pertama (nama[0])
        if ('b'  in karakter):
            jumcow+=1
        elif ('d' in karakter):
            jumcow+=1
        elif ('o' in karakter):
            jumcow +=1
        elif ('i' in karakter):
            jumcew +=1
        elif ('a' in karakter):
            jumcew +=1
        elif ('u' in karakter):
            jumcew +=1
        elif ('e' in karakter):
            jumcew +=1
        elif ('t' in karakter):
            jumcew +=1
        elif ('l' in karakter):
            jumcew +=1
    print ("Daftar nama /kata :",list(nama))
    if jumcew>jumcow :
        print("Jenis Kelamin : Perempuan")
    elif jumcew<jumcow :
        print("Jenis Kelamin : Laki-laki")
    else :
        print("Jenis Kelamin : Tidak diketahui")
array(nama)
#hasil percobaan nama : diah eka amalia (perempuan)

#hasil dari beberapa kali percobaan menunjukkan bahwa frekuensi jenis kelamin
#perempuan lebih banyak di banding laki-laki karena feature yang ditentukan untuk
#perempuan lebih banyak sehingga besar kemungkinan nama depan memuat huruf dalam
#kategori perempuan.
