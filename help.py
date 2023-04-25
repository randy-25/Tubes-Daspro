# Prosedur untuk menampilkan help sesuai role

# KAMUS LOKAL

# Algoritma
def help(status,role):
    print("=========== HELP ===========")
    # yg belom login
    if status == 0:
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
        print("3. save")
        print("   Untuk menyimpan data")
    elif status == 1:
        if role == "bandung_bondowoso":
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. summonjin")
            print("   Untuk memanggil jin")
            print("3. hapusjin")
            print("   Untuk menghapus jin")
            print("4. ubahjin")
            print("   Untuk mengubah tipe jin")
            print("5. batchkumpul")
            print("   Untuk mengumpulkan bahan")
            print("6. batchbangun")
            print("   Untuk mengumpulkan jin bangun")
            print("7. laporanjin")
            print("   Untuk mengetahui kinerja jin")
            print("8. laporancandi")
            print("   Untuk mengetahui proses pembangunan candi")
        elif role == "roro_jonggrang" :
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. hancurkancandi")
            print("   Untuk menghancurkan candi yang tersedia")
            print("3. ayamberkokok")
            print("   Untuk menyelesaikan permainan.")
        elif role == "jin_pengumpul" :
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. kumpul")
            print("   Untuk mengumpulkan resource candi")
        elif role == "jin_pembangun":
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. bangun")
            print("   Untuk membangun candi")