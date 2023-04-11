from personalCommand import cekLogin

#Fungsi login
def login(status, username):
    if status == 1:
        print("Login gagal!")
        print("Anda telah login dengan username " + username +" silahkan lakukan “logout” sebelum melakukan login kembali.")
        return status,username
    else:
        username = input("Username: ")
        password = input("Password: ")

        codeLogin = cekLogin(username,password)
        if codeLogin == 3:
            print("Selamat Datang", username + '!')
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
            return 1,username
        elif codeLogin == 2:
            print("Password Salah!")
            return 2,''
        elif codeLogin == 1:
            print("Username tidak terdaftar!")
            return 3,''
    
            