def getCategory(f) -> int:
    count = 1
    fString = f.readlines(1)
    for i in range (len(fString[0])):
        if fString[0][i] == ';':
            count += 1
    return count

#Fungsi mencari banyak baris dalam file
def file(f) -> tuple:
    sum = 0
    lineString = ''
    for line in f.readlines() :
        sum += 1
        lineString += line
    return sum,lineString

#Fungsi mengambil data category dan length lalu dimasukkan ke matriks
def getUser(length:int,category:int,StringOF:str) ->list:
    data = [['' for i in range (category)] for j in range(length)]
    i = 0
    j = 0
    for k in range(len(StringOF)) :
        if StringOF[k] == ';':
            j += 1
        if StringOF[k] == '\n':
            j = 0
            i+=1
        if i >=(length) :
            break
        if StringOF[k] != ';' and StringOF[k] != '\n':
            data[i][j] += StringOF[k]    
    return data

def getCandi(length:int,category:int,StringOF:str) ->list:
    data = [['' for i in range (category)] for j in range(length)]
    i = 0
    j = 0
    for k in range(len(StringOF)) :
        if StringOF[k] == ';':
            j += 1
        if StringOF[k] == '\n':
            j = 0
            i+=1
        if i >=(length) :
            break
        if StringOF[k] != ';' and StringOF[k] != '\n':
            data[i][j] += StringOF[k]
    countJump = 0   
    count = 0
    for i in range(length):
        if data[i][0] != count :
            countJump += int(data[i][0]) - count
            count = int(data[i][0])
        count += 1
    changes = length + countJump
    dataX = [[None for i in range(category)] for j in range(changes)]
    for i in range(length):
        for j in range(category):
            dataX[int(data[i][0])][j] = data[i][j]
    return dataX, changes

def getBangunan(length:int,category:int,StringOF:str) ->list:
    if length == 0:
        data = [['pasir','butiran dari pantai','0'],['batu','benda yang keras','0'],['air','benda cair','0']]
        length = 3
    else:
        data = [['' for i in range (category)] for j in range(length)]
        i = 0
        j = 0
        for k in range(len(StringOF)) :
            if StringOF[k] == ';':
                j += 1
            if StringOF[k] == '\n':
                j = 0
                i+=1
            if i >=(length) :
                break
            if StringOF[k] != ';' and StringOF[k] != '\n':
                data[i][j] += StringOF[k]    
    return data,length

def appendX(X,listX:list,length:int)->list :
    newListX = [None for i in range(length+1)]
    for i in range(length):
        newListX[i] = listX[i]
    newListX[length] = X
    return newListX

def cekJumlahCandi(candiData, candiLength):
    jumlahCandi = 0
    for i in range(candiLength):
        if candiData[i][0] != None and candiData[i][0] != 'None':
            jumlahCandi += 1
    return jumlahCandi

def stringCompare(stringA,stringB):
    a = -999
    b = -999
    abjadListGede = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    abjadListKecil = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(26):
        if stringA[0] == abjadListKecil[i] :
            a = i
        if stringB[0] == abjadListKecil[i] :
            b = i
        if stringA[0] == abjadListGede[i] :
            a = i
        if stringB[0] == abjadListGede[i] :
            b = i
    return a,b

def IntToRupiah(angka):
    angka = str(angka)
    dum = ""; dum2 = ""
    for i in range(len(angka)):
        if i < len(angka)-3:
            dum += angka[i]
        elif i >= len(angka)-3:
            dum2 += angka[i]
    final = dum + "." + dum2
    return final

def listToStr(aList,length):
    stringList = ''
    for i in range(length):
        if aList[i][0] != None:
            dummySTR = str(aList[i])
            for j in range(len(dummySTR)):
                if dummySTR[j] == '[':
                    stringList += '\n'
                elif dummySTR[j] == ',' and dummySTR[j-1] != ']':
                    stringList += ';'
                elif dummySTR[j] != ']' and dummySTR[j] != ',' and dummySTR[j] != "'" :
                    if dummySTR[j] == " " and dummySTR[j-1] != ",":
                        stringList += dummySTR[j]
                    elif dummySTR[j] != " ":
                        stringList += dummySTR[j]
    return stringList