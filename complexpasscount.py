specialchars = ["!","@","#","%","^","&","*","~"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
complexfound = []
passdone = 0
def countcomplex(wordlist):
    passcount = 0
    for password in wordlist:
        if complexfound.count(password) == 0:
            password = str(password)
            count = 0
            check = 0
            if len(password) > 8:
                count = count + 1
            for char in specialchars:
                if check == 0 and password.count(char) > 0:
                    count = count + 1
                    check = 1
            check = 0
            for num in numbers:
                if check == 0 and password.count(num) > 0:
                    count = count + 1
                    check = 1
            check = 0
            for i in range(0, len(password)):
                if password[i].isupper() == True and check == 0:
                    count = count + 1
                    check = 1
            if count > 2:                
                complexfound.append(password)
            passcount = passcount + 1
            print(passcount)

with open('SecLists-master/Passwords/Leaked-Databases/rockyou.txt',  errors="ignore") as f:
    rockyou = f.readlines()
    countcomplex(rockyou)


with open('SecLists-master/Passwords/Leaked-Databases/elitehacker.txt',  errors="ignore") as f:
    elitehacker = f.readlines()
    countcomplex(elitehacker)

with open('SecLists-master/Passwords/Leaked-Databases/honeynet.txt',  errors="ignore") as f:
    honey = f.readlines()
    countcomplex(honey)

with open('SecLists-master/Passwords/Leaked-Databases/Ashley-Madison.txt',  errors="ignore") as f:
    ashley = f.readlines()
    countcomplex(ashley)

with open('SecLists-master/Passwords/Leaked-Databases/Lizard-Squad.txt',  errors="ignore") as f:
    lizard = f.readlines()
    countcomplex(lizard)

with open('SecLists-master/Passwords/Leaked-Databases/phpbb.txt',  errors="ignore") as f:
    phpbb = f.readlines()
    countcomplex(phpbb)

with open('SecLists-master/Passwords/Leaked-Databases/000webhost.txt',  errors="ignore") as f:
    webhost = f.readlines()
    countcomplex(webhost)

with open('SecLists-master/Passwords/Leaked-Databases/NordVPN.txt',  errors="ignore") as f:
    nordvpn = f.readlines()
    countcomplex(nordvpn)


with open("complexpassfound.txt","w", errors="ignore") as file:
    for com in complexfound:
        file.write(com)
    print("complexpassfound.txt was created")

#for com in complexfound:
#    print(com)