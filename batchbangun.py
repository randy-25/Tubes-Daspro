import random
import personalCommand


def batchbangun(userData,userLength,candiData,candiLength,bangunanData):
    jumlahJinPembangun = 0
    indexJinPembangun = []
    for i in range(userLength):
        if userData[i][2] == "jin_pembangun":
            indexJinPembangun = personalCommand.appendX(i,indexJinPembangun,jumlahJinPembangun)
            jumlahJinPembangun += 1
    
    if jumlahJinPembangun == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        return candiData,candiLength,bangunanData
    dataBatch = [[None for i in range (4)] for j in range(jumlahJinPembangun)]

    totalPasir = 0
    totalBatu = 0
    totalAir = 0

    for i in range(jumlahJinPembangun):
        pasir = random.randint(1, 5)    # kalau mengerjakan b1 bisa diganti
        batu = random.randint(1, 5)
        air = random.randint(1, 5)
        dataBatch[i][0] = userData[indexJinPembangun[i]][0]
        dataBatch[i][1] = pasir
        dataBatch[i][2] = batu
        dataBatch[i][3] = air

        totalPasir += pasir
        totalBatu += batu
        totalAir += air
    if int(bangunanData[0][2]) < totalPasir or int(bangunanData[1][2]) < totalBatu or int(bangunanData[2][2]) < totalAir :
        print(f"Mengerahkan {jumlahJinPembangun} jin untuk membangun candi dengan total bahan {totalPasir} pasir, {totalBatu} batu, dan {totalAir} air.")
        printSTR = "Bangun gagal. Kurang "
        penandaPasir = False
        penandaBatu = False 
        if int(bangunanData[0][2]) < totalPasir:
            printSTR += str((totalPasir - int(bangunanData[0][2]))) + " pasir"
            penandaPasir = True
        if int(bangunanData[1][2]) < totalBatu :
            if penandaPasir:
                printSTR += ", " + str((totalBatu - int(bangunanData[1][2]))) + " batu"
            else :
                printSTR += str((totalBatu - int(bangunanData[1][2]))) + " batu"
            penandaBatu = True
        if int(bangunanData[2][2]) < totalAir:
            if penandaBatu or penandaPasir:
                printSTR += ", " + str((totalAir - int(bangunanData[2][2]))) + " air"
            else:
                printSTR += str((totalAir - int(bangunanData[2][2]))) + " batu"
        printSTR += "."
        print(printSTR)
        return candiData,candiLength,bangunanData
    else :
        jumlahCandi = personalCommand.cekJumlahCandi(candiData,candiLength)
        if jumlahCandi <= 99:
            j = 0
            for i in range(candiLength):
                if candiData[i][0] == None or candiData[i][0] == 'None' :
                    if j < jumlahJinPembangun:
                        candiData[i][0] = str(i)
                        candiData[i][1] = (dataBatch[j][0])
                        candiData[i][2] = str(dataBatch[j][1])
                        candiData[i][3] = str(dataBatch[j][2])
                        candiData[i][4] = str(dataBatch[j][3])
                        jumlahCandi += 1
                        j += 1
                    else :
                        break
            if j < jumlahJinPembangun : #ada yang tersisa tidak dari none
                for i in range(j,jumlahJinPembangun):
                    if jumlahCandi <= 99:
                        candiData = personalCommand.appendX([str(candiLength),dataBatch[j][0],str(dataBatch[j][1]),str(dataBatch[j][2]),str(dataBatch[j][3])],candiData,candiLength)
                        candiLength += 1
                        jumlahCandi += 1
                        j += 1
            bangunanData[0][2] = str(int(bangunanData[0][2]) - totalPasir)
            bangunanData[1][2] = str(int(bangunanData[1][2]) - totalBatu)
            bangunanData[2][2] = str(int(bangunanData[2][2]) - totalAir)
            print(f"Mengerahkan {jumlahJinPembangun} jin untuk membangun candi dengan total bahan {totalPasir} pasir, {totalBatu} batu, dan {totalAir} air.")
            print(f"Sisa candi yang perlu dibangun: {100-jumlahCandi}.")
            return candiData,candiLength,bangunanData
        else: #jumlah candi sudah lebih dari 100, tetap dibangun dan tetap dikurang tetapi sisa candi tetap 0
            print(f"Mengerahkan {jumlahJinPembangun} jin untuk membangun candi dengan total bahan {totalPasir} pasir, {totalBatu} batu, dan {totalAir} air.")
            print(f"Sisa candi yang perlu dibangun: {100-jumlahCandi}.")
            bangunanData[0][2] = str(int(bangunanData[0][2]) - totalPasir)
            bangunanData[1][2] = str(int(bangunanData[1][2]) - totalBatu)
            bangunanData[2][2] = str(int(bangunanData[2][2]) - totalAir)
            return candiData,candiLength,bangunanData