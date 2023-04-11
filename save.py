import os.path

def save(fileContent): #file content dari array
    folderName = input("Masukkan nama folder: ")
    folder = './save/' + folderName
    filePath = os.path.join(folder, "save.csv")
    if not os.path.isdir(folder):
        os.mkdir(folder)
    with open(filePath, 'w+') as f:
        f.write(fileContent)
        
