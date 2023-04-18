import save

def exit(candi,bahanBangunan):
    confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while confirm != 'y' and confirm != 'n':
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if confirm == 'y' :
        save.save(candi,bahanBangunan) # file content dari array
        return 0
    elif confirm == 'n':
        return 0