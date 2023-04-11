from login import login
from logout import logout

# cek sudah login apa belom di sini
status = 0
username = ''
while True:
    command = input("Masukkan Command: ")
    if command == 'login' :
        status,username = login(status,username)
    elif command == 'logout':
        status = logout(status)


