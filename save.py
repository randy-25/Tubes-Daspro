import os.path
import personalCommand

# Prosedur untuk menyimpan data permainan

# KAMUS LOKAL
# folderName, folder: string
# filePath1, filePath2, filePath3 : string

# Algoritma
def save(userData,userLength,candiData,candiLength,bangunanData,bangunanLength): #file content dari array
    userData = personalCommand.listToStr(userData,userLength)
    userData = "username;password;role" + userData
    candiData = personalCommand.listToStr(candiData,candiLength)
    candiData = "id;pembuat;pasir;batu;air" + candiData
    bangunanData = personalCommand.listToStr(bangunanData,bangunanLength)
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


