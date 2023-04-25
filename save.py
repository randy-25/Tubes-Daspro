import os.path

def listToStr(aList,length):
    stringList = ''
    for i in range(length):
        if aList[i][0] != None:
            dummySTR = str(aList[i])
            for j in range(len(dummySTR)):
                if dummySTR[j] == '[':
                    stringList += '\n'
                elif dummySTR[j] == ',' and dummySTR[j-1] != ']':
                    stringList += ';'
                elif dummySTR[j] != ']' and dummySTR[j] != ',' and dummySTR[j] != "'" :
                    if dummySTR[j] == " " and dummySTR[j-1] != ",":
                        stringList += dummySTR[j]
                    elif dummySTR[j] != " ":
                        stringList += dummySTR[j]
    return stringList
        
def save(userData,userLength,candiData,candiLength,bangunanData,bangunanLength): #file content dari array
    userData = listToStr(userData,userLength)
    userData = "username;password;role" + userData
    candiData = listToStr(candiData,candiLength)
    candiData = "id;pembuat;pasir;batu;air" + candiData
    bangunanData = listToStr(bangunanData,bangunanLength)
    bangunanData = "nama;deskripsi;jumlah" + bangunanData
    folderName = input("Masukkan nama folder: ")
    folder = './save/' + folderName
    if not os.path.exists('save'):
        os.mkdir('save')

    filePath1 = os.path.join(folder, "user.csv")
    filePath2 = os.path.join(folder, "candi.csv")
    filePath3 = os.path.join(folder, "bahan_bangunan.csv")
    if not os.path.exists(folder):
        os.mkdir(folder)

    with open(filePath1, 'w') as f:
        f.write(userData)
    with open(filePath2, 'w') as f:
        f.write(candiData)
    with open(filePath3, 'w') as f:
        f.write(bangunanData)
    print("Data berhasil disimpan")


