def hancurkanCandi(CandiData:list,CandiLength:int)->list:
    id = input("Masukkan ID candi: ")
    if int(id) > CandiLength-1 :
        print("Tidak ada candi dengan ID tersebut.")
        return CandiData
    if CandiData[int(id)][0] == None or CandiData[int(id)][0] == 'None':
        print("Tidak ada candi dengan ID tersebut.")
        return CandiData
    
    confirm = input("Apakah anda yakin ingin menghancurkan candi ID: %s (Y/N)? "%id)
    if confirm == "Y" or confirm == 'y':
        for i in range(CandiLength):
            if CandiData[i][0] == id:
                CandiData[i][0] = None
                CandiData[i][1] = None
                CandiData[i][2] = None
                CandiData[i][3] = None
                CandiData[i][4] = None
                print("Candi telah berhasil dihancurkan.")
    return CandiData