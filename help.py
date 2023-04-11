def help(status,role):
    print("=========== HELP ===========")
    # yg belom login
    if status == 0:
        print("1. login")
        print("\tUntuk masuk menggunakan akun")
        print("2. exit")
        print("\tUntuk keluar dari program dan kembali ke terminal")
    elif status == 1:
        if role == "bandung_bondowoso":
            print("Bandung bondowoso")
        elif role == "roro_jongrang" :
            print("roro jongrang")
        elif role == "jin" :
            print("role")