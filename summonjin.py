import personalCommand

def cekUsername(userData,userLength,username): # -> Boolean
        # Fungsi untuk mengecek keberadaan username didalam array username
        for i in range(userLength):
            if username == userData[i][0]:
                return True
        return False

def summonjin(userData,userLength):
    if userLength < 102:
        print("Jenis jin yang dapat dipanggil: ")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi \n\n")
        jenis_jin = input("Masukkan jenis jin yang ingin dipanggil: ")
        while (jenis_jin != '1' and jenis_jin != '2'):
            print(f"Tidak ada jenis jin bernomor “{jenis_jin}”!")
            print("\n\n")
            print("Jenis jin yang dapat dipanggil: ")
            print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print("(2) Pembangun - Bertugas membangun candi \n\n")

            jenis_jin = input("Masukkan jenis jin yang ingin dipanggil: ")

        # Jika memilih jin Pengumpul
        if (jenis_jin == '1'):
            print("Memilih Jin Pengumpul\n")
            username = input("Masukkan username jin:")
            # Kasus Username Udah Diambil
            while (cekUsername(userData,userLength,username)):
                print(f"Username {username} sudah diambil\n")
                username = input("Masukkan username jin:")        
            password = input("Masukkan password jin:")
            # Kasus Password Kurang bukan diantara 5-25 karakter
            while (not(5 <= len(password) <= 25)):
                print("\nPassword panjangnya harus 5-25 karakter!")
                password = input("Masukkan password jin:")
            #append data baru ke user data
            userData = personalCommand.appendX([username,password,'jin_pengumpul'],userData,userLength)

        elif (jenis_jin =='2'):
            print("Memilih Jin Pembangun\n")
            username = input("Masukkan username jin:")
            # Kasus Username Udah Diambil
            while (cekUsername(userData,userLength,username)==True):
                print(f"Username {username} sudah diambil\n")
                username = input("Masukkan username jin:")

            password = input("Masukkan password jin:")
            # Kasus Password Kurang bukan diantara 5-25 karakter
            while (not(5 <= len(password) <= 25)):
                print("\nPassword panjangnya harus 5-25 karakter!")
                password = input("Masukkan password jin:")
            #append data baru ke user data
            userData = personalCommand.appendX([username,password,'jin_pembangun'],userData,userLength)
        return userData,(userLength + 1)
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        return userData,userLength

#user data disimpan terlebih dahulu, jika di save diakhir baru memasukkan ke file csv