import save

def exit():
    confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while confirm != 'y' or confirm != 'n':
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if confirm == 'y' :
        save.save("asdas") # file content dari array
        return 0
    elif confirm == 'n':
        return 0