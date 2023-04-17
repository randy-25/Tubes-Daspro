def hancurkanCandi(CandiData:list,CandiLength:int)->list:
    id = input("Masukkan ID candi: ")
    confirm = input("Apakah anda yakin ingin menghancurkan candi ID: %s (Y/N)? "%id)
    if confirm == "Y":
        for i in range(CandiLength):
            if int(id) > CandiLength :
                print("Tidak ada candi dengan ID tersebut.")
                return CandiData
            if CandiData[i][0] == id:
                CandiData[i][0] = None
                CandiData[i][1] = None
                CandiData[i][2] = None
                CandiData[i][3] = None
                CandiData[i][4] = None
                print("Candi telah berhasil dihancurkan.")
    return CandiData