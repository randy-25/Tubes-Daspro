#Fungsi mencari banyak baris dalam file
def fileLength(f):
    sum = 0
    for line in f.readlines() :
        sum += 1
    return sum

#variabel global banyak baris di file csv
with open ('./database/user.csv','r') as f:
    x = fileLength(f) -1

#Fungsi mengambil data username, passsword, dan role lalu dimasukkan ke matriks
def getData(f):
    data = [['' for i in range (x+1)] for j in range(3)]
    i = 0
    j = 0
    for char in f.read() :
        if char == ';':
            i += 1
        if char == '\n':
            i = 0
            j+=1
        if j >=(x+1) :
            break
        if char != ';' and char != '\n':
            data[i][j] += char    
    dataX = [['' for i in range(x)] for j in range(3)]
    for i in range(3):
        for j in range(x):
            dataX[i][j] = data[i][j+1]
    return dataX     

#Fungsi cek login
def cekLogin(username,password):    
    with open('./database/user.csv','r') as f:
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

