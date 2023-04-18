import os.path

def listToStr(aList):
    aList = str (aList)
    stringList = ''
    for i in range(1,len(aList)):
        if aList[i] == '[':
            stringList += '\n'
        elif aList[i] == ',' and aList[i-1] != ']':
            stringList += ';'
        elif aList[i] != ']' and aList[i] != ',' and aList[i] != "'" :
            if aList[i] == " " and aList[i-1] != ",":
                stringList += aList[i]
            elif aList[i] != " ":
                stringList += aList[i]
    return stringList

def save(user,candi,bahanBangunan): #file content dari array
    user = listToStr(user)
    user = "username;password;role" + user
    candi = listToStr(candi)
    candi = "id;pembuat;pasir;batu;air" + candi
    bahanBangunan = listToStr(bahanBangunan)
    bahanBangunan = "nama;deskripsi;jumlah" + bahanBangunan
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
        f.write(user)
    with open(filePath2, 'w') as f:
        f.write(candi)
    with open(filePath3, 'w') as f:
        f.write(bahanBangunan)
