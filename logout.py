def logout(status:int)->tuple:
    if status == 1 :
        print("Logout berhasil!")
        return 0,None
    else :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return 0,None