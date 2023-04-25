import personalCommand

# Fungsi untuk mengambil nilai unik pada suatu array atau matriks

# KAMUS LOKAL 
# dataX : array of string
# lengthX : integer

# Algoritma
def getUniqueValue(aList,length):
    dataX = []
    lengthX = 0
    for i in range(length):
        if aList[i][0] != None:
            if lengthX == 0:
                dataX = personalCommand.appendX(aList[i][1],dataX,lengthX)
                lengthX += 1
            else:
                marker = 0
                for j in range(lengthX):
                    if aList[i][1] == dataX[j]:
                        marker += 1
                        break
                if marker == 0:
                    dataX = personalCommand.appendX(aList[i][1],dataX,lengthX)
                    lengthX += 1
    return dataX, lengthX

# Prosedur untuk menngeluarkan nilai dari laporan jin

# KAMUS LOKAL
# totalJin, totalJinPengumpul, totalJinPembangun : integer
# candiMaker : dataArray
# sumMaker : array of integer
# max, min : integer
# jumlahPasir, jumlahBatu, jumlahAir : integer
# jinTerajin, jinTermalas : string

# Algoritma
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
    
    candiMaker,MakerLength = getUniqueValue(candiData,candiLength)
    sumMaker = [0 for i in range (MakerLength)]
    for i in range(MakerLength):
        for j in range(candiLength):
            if candiData[j][0] != None:
                if candiData[j][1] == candiMaker[i]:
                    sumMaker[i] += 1
    max = -999
    min = 999
    for i in range(MakerLength):
        if max < sumMaker[i]:
            max = sumMaker[i]
            jinTerajin = candiMaker[i]
        if min > sumMaker[i]:
            min = sumMaker[i]
            jinTermalas = candiMaker[i]
        if max == sumMaker[i]:
            a,b = personalCommand.stringCompare(jinTerajin,candiMaker[i])
            if a > b:
                jinTerajin = candiMaker[i]
        if min == sumMaker[i]:
            a,b = personalCommand.stringCompare(jinTermalas,candiMaker[i])
            if a < b:
                jinTermalas = candiMaker[i]
    
    jumlahPasir = bangunanData[0][2]
    jumlahBatu = bangunanData[1][2]
    jumlahAir = bangunanData[2][2]
    if MakerLength != 0:
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


