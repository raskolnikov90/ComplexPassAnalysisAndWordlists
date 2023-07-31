with open('ComplexPasswords.txt',  errors="ignore") as f:
    count = 0
    wordlist = f.readlines()
    def func(arg):
        arg = arg.split()
        return int(arg[0])
    wordtrends = []
    scores = []
    wordcount = " "
    for password in wordlist:
        count = count + 1
        print(str(count))
        if(len(password) > 4):
            if wordtrends.count(password[0:4]) == 0:
                wordtrends.append(password[0:4])
            if wordtrends.count(password[0:3]) == 0:
                wordtrends.append(password[0:3])
            wordcount = wordcount + password[0:4] + " "

    for score in wordtrends:
        scores.append(str(wordcount.count(score))  + " " + score)
        
    scores.sort(key=func, reverse=True)

    with open("prefixscores.txt","w", errors="ignore") as file:
        for i in range(500):
            file.write(scores[i] +"\n")
    print("prefixscores.txt was created")

    with open("topprefixnoscore.txt","w", errors="ignore") as file:
        for i in range(0, 500):
            top = scores[i].split()
            if top != []:
                print(top)
                file.write(top[1] +"\n")

    print("topprefixnoscore.txt was created")
    #for com in scores:
    
    #    print(com)
    #to print results without score
    #for com in scores:
    #    com = com.split()
    #    print(com[1])