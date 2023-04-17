#Fungsi cek login
def cekLogin(username:str,password:str,UserData:list,UserLength:list) -> tuple:    
    data = UserData
    code = 0
    for i in range (UserLength):
        if username == data[i][0] :
            if password != data[i][1]:
                return 2,None
            elif username == data[i][0] and password == data[i][1] :
                return 3,data[i][2]
        else :
            code = 1
    return code,None

#Fungsi login
def login(status:str, username:str,UserData:list,UserLength:list) -> tuple:
    if status == 1:
        print("Login gagal!")
        print("Anda telah login dengan username " + username +" silahkan lakukan “logout” sebelum melakukan login kembali.")
        return status,username
    else:
        username = input("Username: ")
        password = input("Password: ")

        codeLogin,role = cekLogin(username,password,UserData,UserLength)
        if codeLogin == 3:
            print("Selamat Datang", username + '!')
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
            return 1,username,role
        elif codeLogin == 2:
            print("Password Salah!")
            return 2,'',None
        elif codeLogin == 1:
            print("Username tidak terdaftar!")
            return 3,'',None
    
            