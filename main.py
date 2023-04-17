import login
import logout
import load
import help

if __name__ == "__main__" :
    UserData,UserLength,CandiData,CandiLength,BangunanData,BangunanLength = load.Main()
    #kalo datanya ga none (nama foldernya bener)
    if UserData != None or UserLength != None or CandiData != None or CandiLength != None or BangunanData != None or BangunanLength != None :
        #cek sudah login apa belom di sini
        status = 0
        username = ''
        role = None
        while True:
            command = input("Masukkan Command: ")
            if command == 'login' :
                status,username,role = login.login(status,username,UserData,UserLength)
            elif command == 'help':
                help(status,role)
            elif command == 'logout':
                status,role = logout.logout(status)
            elif status == 1:
                if role == "bandung_bondowoso":
                    #masukkan fungsi2 bandung bondowoso di sini
                    print("bandung_bondowoso")
                elif role == "roro_jonggrang":
                    print("roro_jonggrang")
                elif role == "jin_pengumpul":
                    #fungsi2 jin pengumpul
                    print("jin_pengumpul")
                elif role == "jin_pembangun":
                    #fungsi2 jin pembangun
                    print("jin_pembangun")


       

