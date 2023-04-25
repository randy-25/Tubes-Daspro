import random

# Fungsi untuk mengerahkan seluruh jin pengumpul untuk mengumpulkan bahan

# KAMUS LOKAL 
# jumlahJin : integer
# totalPasir, totalBatu, totalAir : integer
# pasir, batu, air : integer

# Algoritma
def batchkumpul(userData:list,userLength:int,bangunanData:list) -> list:
    jumlahJin = 0
    for i in range(userLength):
        if userData[i][2] == 'jin_pengumpul':
            jumlahJin += 1
    if jumlahJin == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        return bangunanData
    totalPasir = 0
    totalBatu = 0
    totalAir = 0
    for i in range(jumlahJin):
        pasir = random.randint(0, 5)    # kalau mengerjakan b1 bisa diganti
        batu = random.randint(0, 5)
        air = random.randint(0, 5)

        totalPasir += pasir
        totalBatu += batu
        totalAir += air
        
    bangunanData[0][2] = str(int(bangunanData[0][2]) + totalPasir)
    bangunanData[1][2] = str(int(bangunanData[1][2]) + totalBatu)
    bangunanData[2][2] = str(int(bangunanData[2][2]) + totalAir)
    print(f"Mengerahkan {jumlahJin} jin untuk mengumpulkan bahan.")
    print(f"Jin menemukan total {totalPasir} pasir, {totalBatu} batu, dan {totalAir} air.")
    return bangunanData