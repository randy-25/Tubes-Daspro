import save

# Fungsi untuk exit

# KAMUS LOKAL
# confirm : character

# Algoritma
def exit(userData,userLength,candiData, candiLength ,bangunanData, bangunanLength):
    confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while confirm != 'y' and confirm != 'n':
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if confirm == 'y' :
        save.save(userData,userLength,candiData, candiLength ,bangunanData, bangunanLength) # file content dari array
        return 0
    elif confirm == 'n':
        return 0