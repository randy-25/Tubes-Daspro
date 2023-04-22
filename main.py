import login
import logout
import load
import help
import save
import exit
import hancurkanCandi,ayamBerkokok #roro
import summonjin, hapusjin, ubahJin,batchkumpul, batchbangun, laporanjin, laporancandi #bondowoso
import kumpul #jin pengumpul
import bangun #jin pembangun

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
                exit = exit.exit(UserData,UserLength,CandiData,CandiLength,BangunanData,BangunanLength)
                if exit == 0:
                    break
            if status == 1:
                if role == "bandung_bondowoso":
                    if command == 'summonjin':
                        UserData,UserLength = summonjin.summonjin(UserData,UserLength)
                    elif command == 'hapusjin':
                        UserData,CandiData = hapusjin.HapusUser(UserData,UserLength,CandiData,CandiLength)
                    elif command == 'ubahjin':
                        UserData = ubahJin.ubahJin(UserData,UserLength)
                    elif command == 'batchkumpul':
                        BangunanData = batchkumpul.batchkumpul(UserData,UserLength,BangunanData)
                    elif command == 'batchbangun':
                        CandiData,CandiLength,BangunanData = batchbangun.batchbangun(UserData,UserLength,CandiData,CandiLength,BangunanData)
                    elif command == 'laporanjin':
                        laporanjin.laporanjin(UserData,UserLength,CandiData,CandiLength,BangunanData,BangunanLength)
                    elif command == 'laporancandi':
                        laporancandi.laporancandi(CandiData,CandiLength)
                    elif command == 'save':
                        save.save(UserData,UserLength,CandiData,CandiLength,BangunanData,BangunanLength)
                elif role == "roro_jonggrang":
                    if command == 'logout':
                        status,role = logout.logout(status)
                    elif command == 'hancurkancandi':
                        CandiData = hancurkanCandi.hancurkanCandi(CandiData,CandiLength)
                    elif command == 'ayamberkokok':
                        ayamBerkokok.ayamBerkokok(CandiData,CandiLength)
                        break
                    elif command == 'save':
                        save.save(UserData,UserLength,CandiData,CandiLength,BangunanData,BangunanLength)
                elif role == "jin_pengumpul":
                    if command == "kumpul":
                        BangunanData = kumpul.kumpul(BangunanData)
                elif role == "jin_pembangun":
                    if command == "bangun":
                        CandiData,CandiLength,BangunanData = bangun.bangun(username,CandiData,CandiLength,BangunanData)
                    



       

