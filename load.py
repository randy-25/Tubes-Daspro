import os
import argparse


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("load",help="Berikan nama folder yang ingin di load!",nargs='?')
    args = parser.parse_args()
    if args.load is None:
        print("Tidak ada nama folder yang diberikan!")
    elif os.path.isdir(args.load) != True :
        print("Folder " + args.load + " tidak ditemukan.")
    elif os.path.isdir(args.load):
        # file di dalamnya akan di load (nanti diimplementasikan)
        print("Selamat datang di program “Manajerial Candi")