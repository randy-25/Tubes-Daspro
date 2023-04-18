def ubahJin(userData,userLength):
    namaJin = input("Masukkan username jin : ")
    cek = False 
    index = -999
    for i in range (userLength):
        if namaJin == userData[i][0]:
            cek = True
            index = i
    if cek :
        if userData[index][2] == 'jin_pengumpul':
            confirm = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
            if confirm == 'y' or confirm == "Y":
                userData[index][2] = 'jin_pembangun'
                return userData
            else :
                print("Jin tidak jadi diubah")
                return userData
        elif userData[index][2] == 'jin_pembangun':
            confirm = input('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul" (Y/N)? ')
            if confirm == 'y' or confirm == "Y":
                userData[index][2] = 'jin_pengumpul'
                return userData
            else :
                print("Jin tidak jadi diubah")
                return userData
    else:
        print("Tidak ada jin dengan username tersebut.")
        return userData
