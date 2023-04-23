def IntToRupiah(angka):
    angka = str(angka)
    dum = ""; dum2 = ""
    for i in range(len(angka)):
        if i < len(angka)-3:
            dum += angka[i]
        elif i >= len(angka)-3:
            dum2 += angka[i]
    final = dum + "." + dum2
    return final

def laporancandi(candiData,candiLength):
    totalCandi = 0
    totalPasir = 0
    totalBatu = 0
    totalAir = 0

    hargaPasir = 0
    hargaBatu = 0
    hargaAir = 0

    hargaCandiTermahal = -999999
    hargaCandiTermurah = 999999

    idCandiTermahal = 0
    idCandiTermurah = 0

    for i in range(candiLength):
        if candiData[i][0] != None and candiData[i][0] != 'None':
            totalCandi += 1
            totalPasir += (int(candiData[i][2]))
            totalBatu += (int(candiData[i][3]))
            totalAir += (int(candiData[i][4]))

            hargaPasir = 10000*(int(candiData[i][2]))
            hargaBatu = 15000*(int(candiData[i][3]))
            hargaAir = 7500*(int(candiData[i][4]))

            if hargaCandiTermahal < (hargaPasir + hargaBatu + hargaAir):
                hargaCandiTermahal = hargaPasir + hargaBatu + hargaAir
                idCandiTermahal = candiData[i][0]
            if hargaCandiTermurah > (hargaPasir + hargaBatu + hargaAir):
                hargaCandiTermurah = hargaPasir + hargaBatu + hargaAir
                idCandiTermurah = candiData[i][0]
    hargaCandiTermahal = IntToRupiah(hargaCandiTermahal)
    hargaCandiTermurah = IntToRupiah(hargaCandiTermurah)

    if totalCandi != 0:
        print(f"> Total Candi: {totalCandi}")
        print(f"> Total Pasir yang digunakan: {totalPasir}")
        print(f"> Total Batu yang digunakan: {totalBatu}")
        print(f"> Total Air yang digunakan: {totalAir}")
        print(f"> ID Candi Termahal: {idCandiTermahal} (Rp {hargaCandiTermahal})")
        print(f"> ID Candi Termurah: {idCandiTermurah} (Rp {hargaCandiTermurah})")
    else:
        print(f"> Total Candi: {totalCandi}")
        print(f"> Total Pasir yang digunakan: {totalPasir}")
        print(f"> Total Batu yang digunakan: {totalBatu}")
        print(f"> Total Air yang digunakan: {totalAir}")
        print(f"> ID Candi Termahal: -")
        print(f"> ID Candi Termurah: -")
