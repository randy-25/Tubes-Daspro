def HapusCandi(namaJin:str,candiData:list,candiLength:int) -> list:
    for i in range(candiLength):
        if namaJin == candiData[i][1]:
            candiData[i][0] = None
            candiData[i][1] = None
            candiData[i][2] = None
            candiData[i][3] = None
            candiData[i][4] = None
    return candiData

def HapusUser(userData,userLength,candiData,candiLength):
    namaJin = input("Masukkan username jin : ")
    cek = False
    index = -999
    for i in range(userLength):
        if namaJin == userData[i][0]:
            index = i
            cek = True

    if cek == False :
        print("Tidak ada jin dengan username tersebut.")
        return userData,candiData
    elif cek == True:
        confirm = input(f"Apakah anda yakin ingin menghapus jin dengan username {namaJin} (Y/N)? ")
        if confirm == 'y' or confirm == 'Y':
            userData[index][0] = None
            userData[index][1] = None
            userData[index][2] = None
            candiData = HapusCandi(namaJin,candiData,candiLength)
            print("Jin Berhasil dihapus")
            return userData,candiData
        elif confirm == 'n' or confirm == 'N':
            print("Jin tidak jadi dihapus")
            return userData,candiData
