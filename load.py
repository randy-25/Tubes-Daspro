import os
import argparse
import personalCommand

# Fungsi untuk menload database dari parent folder ./save

# KAMUS LOKAL
# args.load : string
# UserCategory, CandiCategory, BangunanCategory : integer
# UserLength, CandiLength, BangunanLength : integer
# UserStringOF, CandiStringOF, BangunanStringOF : string

# Algoritma
def load() -> tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument("load",help="Berikan nama folder yang ingin di load!",nargs='?')
    args = parser.parse_args()
    if args.load is None:
        print("Tidak ada nama folder yang diberikan!")
        return  None,None,None,None,None,None
    elif os.path.isdir("./save/" + args.load) != True :
        args.load = "./save/" + args.load
        print("Folder " + args.load + " tidak ditemukan.")
        return  None,None,None,None,None,None
    elif os.path.isdir("./save/" + args.load):
        args.load = "./save/" + args.load
        print('Selamat datang di program “Manajerial Candi"')
        with open (args.load  +'/user.csv','r') as f:
            UserCategory = personalCommand.getCategory(f)
            UserLength,UserStringOF = personalCommand.file(f)
        with open (args.load +'/candi.csv','r') as f:
            CandiCategory = personalCommand.getCategory(f)
            CandiLength,CandiStringOF = personalCommand.file(f)

        with open (args.load +'/bahan_bangunan.csv','r') as f:
            BangunanCategory = personalCommand.getCategory(f)
            BangunanLength,BangunanStringOF = personalCommand.file(f)
        UserData = personalCommand.getUser(UserLength,UserCategory,UserStringOF)
        CandiData, CandiLength = personalCommand.getCandi(CandiLength,CandiCategory,CandiStringOF)
        BangunanData,BangunanLength = personalCommand.getBangunan(BangunanLength,BangunanCategory,BangunanStringOF)
        return UserData,UserLength,CandiData,CandiLength,BangunanData,BangunanLength

