## Read dari File
# Engga tau caranya

user = ["" for i in range (102)]
passw = ["" for i in range(102)]
role = ["" for i in range(102)]
# Panjang array dipilih 102 karena jin maksimum berjumlah 100 dengan Bandung Bondowoso dan Roro Jonggrang

def summonjin(arr_user,arr_password,arr_role,i):
    # i merupakan patokan indeks dari ketiga array.
    def cekUsername(arr,username): # -> Boolean
        # Fungsi untuk mengecek keberadaan username didalam array username
        for i in range(102):
            if username == arr[i]:
                return True
                break  
        return False

    cek = True
    while (cek == True):
        print("Jenis jin yang dapat dipanggil: ")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi \n\n")

        jenis_jin = int(input("Masukkan jenis jin yang ingin dipanggil: "))

        # Jika memilih jin Pengumpul
        if (jenis_jin == 1):
            print("Memilih Jin Pengumpul\n")
            username = input("Masukkan username jin:")
            # Kasus Username Udah Diambil
            while (cekUsername(user,username)==True):
                print(f"Username {username} sudah diambil\n")
                username = input("Masukkan username jin:")
                password = input("Masukkan password jin:")
            password = input("Masukkan password jin:")
            # Kasus Password Kurang bukan diantara 5-25 karakter
            while (not(5 <= len(password) <= 25)):
                print("\nPassword panjangnya harus 5-25 karakter!")
                password = input("Masukkan password jin:")
            user[i]=username
            passw[i]=password
            role[i]= "Jin_Pengumpul"


        elif (jenis_jin ==2):
            print("Memilih Jin Pembangun\n")
            username = input("Masukkan username jin:")
            # Kasus Username Udah Diambil
            while (cekUsername(user,username)==True):
                print(f"Username {username} sudah diambil\n")
                username = input("Masukkan username jin:")
                password = input("Masukkan password jin:")
            password = input("Masukkan password jin:")
            # Kasus Password Kurang bukan diantara 5-25 karakter
            while (not(5 <= len(password) <= 25)):
                print("\nPassword panjangnya harus 5-25 karakter!")
                password = input("Masukkan password jin:")
            user[i]=username
            passw[i]=password
            role[i]= "Jin_Pembangun"

        else:
            print(f"Tidak ada jin bernomor {jenis_jin}")        

## Write arraynya ke file user.csv
# Engga tau caranya