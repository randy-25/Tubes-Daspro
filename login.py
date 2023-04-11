#Fungsi mencari banyak baris dalam file
def fileLength(f):
    sum = -1
    for line in f :
        sum += 1
    return sum

#Fungsi mengambil data username, passsword, dan role lalu dimasukkan ke matriks
def getData(f):
    x = fileLength(f)
    data = [['' for i in range (x)] for i in range(3)]
    i = 0
    f.seek(23)
    j = 0
    for char in f.read() :
        if char == ';':
            i += 1
        if char == '\n':
            i = 0
            j+=1
        if j >=x :
            break
        if char != ';' and char != '\n':
            data[i][j] += char
    return data


#Fungsi cek login
def cekLogin(username,password):
    with open ('user.csv','r') as f:
        x = fileLength(f)
        f.seek(0)
        data = getData(f)
    code = 0
    for i in range (x):
        if username == data[0][i] :
            if password != data[1][i]:
                return 2
            elif username == data[0][i] and password == data[1][i] :
                return 3
        else :
            code = 1
    return code

#Fungsi login
def login():
    username = input("Username: ")
    password = input("Password: ")

    codeLogin = cekLogin(username,password)
    if codeLogin == 3:
        print("Selamat Datang", username + '!')
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return 1
    elif codeLogin == 2:
        print("Password Salah!")
        return 2
    elif codeLogin == 1:
        print("Username tidak terdaftar!")
        return 3
            
            