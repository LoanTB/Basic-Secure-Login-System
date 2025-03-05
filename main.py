import hashlib,os,time

def login(id,pw):
    while len(id) < len(pw):
        id += "\b"#"\x00"
    while len(pw) < len(id):
        pw += "\b"#"\x00"
    idNUM = []
    for a in id:
        idNUM.append(ord(a))
    pwNUM = []
    for a in pw:
        pwNUM.append(ord(a))
    kyNUM = []
    for i in range(len(idNUM)):
        kyNUM.append(idNUM[i]^pwNUM[i])
    ky = ""
    for a in kyNUM:
        ky += chr(a)
    sign = hashlib.sha1(ky.encode('utf-8')).hexdigest()
    if not os.path.exists(sign):
        print("Nom d'utilisateur ou mot de passe erroné.")
        return 1
    key = hashlib.sha256(ky.encode("utf-8")).digest()
    with open(sign+"/Data.txt","rb") as fileIN:
        with open("connexion.txt","wb") as fileOUT:
            i = 0
            while fileIN.peek():
                c = ord(fileIN.read(1))
                j = i % len(key)
                b = bytes([c^key[j]])
                fileOUT.write(b)
                i += 1
    with open("connexion.txt","r") as file:
        data = file.readline()
        if not data[0:-1] == "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Connexion échoué.")
            file.close()
            os.remove("connexion.txt")
            return 1
        while data != "":
            data = file.readline()
            print(data)
    os.remove("connexion.txt")
    return 0

def register(id,pw):
    while len(id) < len(pw):
        id += "\b"#"\x00"
    while len(pw) < len(id):
        pw += "\b"#"\x00"
    idNUM = []
    for a in id:
        idNUM.append(ord(a))
    pwNUM = []
    for a in pw:
        pwNUM.append(ord(a))
    kyNUM = []
    for i in range(len(idNUM)):
        kyNUM.append(idNUM[i]^pwNUM[i])
    ky = ""
    for a in kyNUM:
        ky += chr(a)
    sign = hashlib.sha1(ky.encode('utf-8')).hexdigest()
    if os.path.exists(sign):
        print("Nom d'utilisateur indisponible.")
        return 1
    os.mkdir(sign)
    with open(sign+"/Data.tmp", "w") as file:
        file.write("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n")
        file.write("Date: "+time.ctime()+"\n")
    key = hashlib.sha256(ky.encode("utf-8")).digest()
    with open(sign+"/Data.tmp","rb") as fileIN:
        with open(sign+"/Data.txt","wb") as fileOUT:
            i = 0
            while fileIN.peek():
                c = ord(fileIN.read(1))
                j = i % len(key)
                b = bytes([c^key[j]])
                fileOUT.write(b)
                i += 1
    os.remove(sign+"/Data.tmp")
    return 0

while True:
    os.system("cls")
    mode = input("0-Login 1-Register : ")
    print("")
    id = input("Identifiant: ")
    pw = input("Mot de passe: ")

    if mode == "0":
        login(id,pw)
    else:
        register(id,pw)
    input("...")
