import random
def kumpul(bangunanData):   #f7 (prosedur???)
    # Sudah dibuat fungsi untuk mengubah file bahan bangunan menjadi matriks bangunanData

    # mengumpulkan bahan bahan bangunan
    pasir = random.randint(0, 5)    # kalau mengerjakan b1 bisa diganti
    batu = random.randint(0, 5)
    air = random.randint(0, 5)

    # menuliskan ke matriks
    bangunanData[0][2] = str(int(bangunanData[0][2]) + pasir)
    bangunanData[1][2] = str(int(bangunanData[1][2]) + batu)
    bangunanData[2][2] = str(int(bangunanData[2][2]) + air)

    # output
    print("Jin menemukan", pasir, "pasir,", batu, "batu, dan", air, "air.")
    return bangunanData
