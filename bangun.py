import random
import personalCommand


def bangun(username,candiData,candiLength,bangunanData):
    pasir = random.randint(0, 5)    # kalau mengerjakan b1 bisa diganti
    batu = random.randint(0, 5)
    air = random.randint(0, 5)

    if int(bangunanData[0][2]) < pasir or int(bangunanData[1][2]) < batu or int(bangunanData[2][2]) < air :
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
        return candiData,candiLength,bangunanData
    else :
        jumlahCandi = personalCommand.cekJumlahCandi(candiData,candiLength)
        cek = True
        if jumlahCandi <= 100:
            for i in range(candiLength):
                if candiData[i][0] == None :
                    cek = False
                    candiData[i][0] = i+1
                    candiData[i][1] = username
                    candiData[i][2] = pasir
                    candiData[i][3] = batu
                    candiData[i][4] = air
                    jumlahCandi += 1
                    break
            if cek: #tidak ada yg none
                candiData = personalCommand.appendX([str(candiLength+1),username,str(pasir),str(batu),str(air)],candiData,candiLength)
                candiLength += 1
                jumlahCandi += 1
            bangunanData[0][2] = str(int(bangunanData[0][2]) - pasir)
            bangunanData[1][2] = str(int(bangunanData[1][2]) - batu)
            bangunanData[2][2] = str(int(bangunanData[2][2]) - air)
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100-jumlahCandi}.")
            return candiData,candiLength,bangunanData
        else: #jumlah candi sudah lebih dari 100, tetap dibangun dan tetap dikurang tetapi sisa candi tetap 0
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: 0.")
            bangunanData[0][2] = str(int(bangunanData[0][2]) - pasir)
            bangunanData[1][2] = str(int(bangunanData[1][2]) - batu)
            bangunanData[2][2] = str(int(bangunanData[2][2]) - air)
            return candiData,candiLength,bangunanData
