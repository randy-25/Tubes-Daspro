def logout(status):
    if status == 1 :
        return 0
    elif status == 0:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return 0