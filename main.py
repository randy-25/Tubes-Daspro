import login
import logout
import load
import help
import save
import exit
import hancurkanCandi,ayamBerkokok #roro

if __name__ == "__main__" :
    UserData,UserLength,CandiData,CandiLength,BangunanData,BangunanLength = load.Main()
    #kalo datanya ga none (nama foldernya bener)
    if UserData != None or UserLength != None or CandiData != None or CandiLength != None or BangunanData != None or BangunanLength != None :
        #cek sudah login apa belom di sini
        status = 0
        username = ''
        role = None
        #program start
        while True:
            command = input(">>> ")
            if command == 'login' :
                status,username,role = login.login(status,username,role,UserData,UserLength)
            elif command == 'help':
                help.help(status,role)
            elif command == 'logout':
                status,role = logout.logout(status)
            elif command == 'exit':
                exit = exit.exit(CandiData,BangunanData)
                if exit == 0:
                    break
            if status == 1:
                if role == "bandung_bondowoso":
                    #masukkan fungsi2 bandung bondowoso di sini
                    print("bandung_bondowoso")
                elif role == "roro_jonggrang":
                    if command == 'logout':
                        status,role = logout.logout(status)
                    elif command == 'hancurkancandi':
                        CandiData = hancurkanCandi.hancurkanCandi(CandiData,CandiLength)
                    elif command == 'ayamberkokok':
                        ayamBerkokok.ayamBerkokok(CandiData,CandiLength)
                        print("\n\nSaving Data... \n")
                        save.save(CandiData,BangunanData)
                        break
                    elif command == 'save':
                        save.save(CandiData,BangunanData)
                elif role == "jin_pengumpul":
                    #fungsi2 jin pengumpul
                    print("jin_pengumpul")
                elif role == "jin_pembangun":
                    #fungsi2 jin pembangun
                    print("jin_pembangun")


       

