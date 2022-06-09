import socket

site = input("Taramak istediğiniz site: ")
target = socket.gethostbyname(site) 

for port in range(1,101):
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = soket.connect_ex((target,port))
        if result ==0:
            print(f"[+] {port} Port -> OPEN")
        soket.close()
    except(ConnectionRefusedError):
        continue
    
print("Tarama İşlemi Bitti.")

