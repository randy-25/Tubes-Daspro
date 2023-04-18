def cekUser(laporCandi, candiMaker,totalJinPembangun):
        for i in range(totalJinPembangun):
            if candiMaker == laporCandi[i][0]:
                return True,i

def stringCompare(stringA,stringB):
    a = -999
    b = -999
    abjadListGede = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    abjadListKecil = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(26):
        if stringA[0] == abjadListKecil[i] :
            a = i
        if stringB[0] == abjadListKecil[i] :
            b = i
        if stringA[0] == abjadListGede[i] :
            a = i
        if stringB[0] == abjadListGede[i] :
            b = i
    return a,b

def laporanjin(userData,userLength,candiData,candiLength,bangunanData,bangunanLength):
    totalJin = 0
    totalJinPengumpul = 0
    totalJinPembangun = 0
    for i in range(userLength):
        if userData[i][2] == "jin_pengumpul" or userData[i][2] == "jin_pembangun":
            totalJin += 1
            if userData[i][2] == "jin_pengumpul" :
                totalJinPengumpul += 1
            elif userData[i][2] == "jin_pembangun":
                totalJinPembangun += 1
    
    laporCandi = [[None,0] for j in range(totalJinPembangun)]
    k = 0
    for i in range (userLength) :
        if userData[i][2] == "jin_pembangun":
            laporCandi[k][0] = userData[i][0]
            k += 1

    for i in range(candiLength):
        cek,j = cekUser(laporCandi,candiData[i][1],totalJinPembangun)
        if cek:
            laporCandi[j][1] += 1
    max = -999
    min = 999
    for i in range(totalJinPembangun):
        if max < laporCandi[i][1]:
            max = laporCandi[i][1]
            jinTerajin = laporCandi[i][0]
        if min > laporCandi[i][1]:
            min = laporCandi[i][1]
            jinTermalas = laporCandi[i][0]
        if max == laporCandi[i][1]:
            a,b = stringCompare(jinTerajin,laporCandi[i][0])
            if a > b:
                jinTerajin = laporCandi[i][0]
        if min == laporCandi[i][1]:
            a,b = stringCompare(jinTermalas,laporCandi[i][0])
            if a < b:
                jinTermalas = laporCandi[i][0]
    
    jumlahPasir = bangunanData[0][2]
    jumlahBatu = bangunanData[1][2]
    jumlahAir = bangunanData[2][2]
    if totalJinPembangun != 0:
        print(f"> Total Jin: {totalJin}")
        print(f"> Total Jin Pengumpul: {totalJinPengumpul}")
        print(f"> Total Jin Pembangun: {totalJinPembangun}")
        print(f"> Jin Terajin: {jinTerajin}")
        print(f"> Jin Termalas: {jinTermalas}")
        print(f"> Jumlah Pasir: {jumlahPasir} unit")
        print(f"> Jumlah Air: {jumlahAir} unit")
        print(f"> Jumlah Batu: {jumlahBatu} unit")
    else:
        print(f"> Total Jin: {totalJin}")
        print(f"> Total Jin Pengumpul: {totalJinPengumpul}")
        print(f"> Total Jin Pembangun: {totalJinPembangun}")
        print(f"> Jin Terajin: -")
        print(f"> Jin Termalas: -")
        print(f"> Jumlah Pasir: {jumlahPasir} unit")
        print(f"> Jumlah Air: {jumlahAir} unit")
        print(f"> Jumlah Batu: {jumlahBatu} unit")


