import login
import logout
import load

if __name__ == "__main__" :
    UserData,UserLength,CandiData,CandiLength,BangunanData,BangunanLength = load.Main()
    #kalo datanya ga none (nama foldernya bener)
    if UserData != None or UserLength != None or CandiData != None or CandiLength != None or BangunanData != None or BangunanLength != None :
        #cek sudah login apa belom di sini
        status = 0
        username = ''
        while True:
            command = input("Masukkan Command: ")
            if command == 'login' :
                status,username = login.login(status,username,UserData,UserLength)
            elif command == 'logout':
                status = logout.logout(status)


       

