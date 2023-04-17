def ayamBerkokok(CandiData:list,CandiLength:int):
    print("Kukuruyuk.. Kukuruyuk..")
    count = 0
    for i in range (CandiLength):
        if CandiData[i][0] != None:
            count += 1
    print("Jumlah Candi:",count)
    if count == 100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    elif count < 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print()
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")