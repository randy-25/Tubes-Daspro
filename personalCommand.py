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
def getData(length:int,category:int,StringOF:str) ->list:
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
    # dataX = [['' for i in range(length)] for j in range(category)]
    return data


def appendX(X,listX:list,length:int)->list :
    newListX = [None for i in range(length+1)]
    for i in range(length):
        newListX[i] = listX[i]
    newListX[length] = X
    return newListX

def cekJumlahCandi(candiData, candiLength):
    jumlahCandi = 0
    for i in range(candiLength):
        if candiData[i][0] != None:
            jumlahCandi += 1
    return jumlahCandi
