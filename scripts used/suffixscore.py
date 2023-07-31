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
            if wordtrends.count(password[-4:len(password)]) == 0:
                wordtrends.append(password[-4:len(password)])
            if wordtrends.count(password[-3:len(password)]) == 0:
                wordtrends.append(password[-3:len(password)])
            if wordtrends.count(password[-2:len(password)]) == 0:
                wordtrends.append(password[-2:len(password)])
            if wordtrends.count(password[-1:len(password)]) == 0:
                wordtrends.append(password[-1:len(password)])
            wordcount = wordcount + password[-4:len(password)] + " "

    for score in wordtrends:
        scores.append(str(wordcount.count(score))  + " " + score)
        
    scores.sort(key=func, reverse=True)

    with open("suffixscores.txt","w", errors="ignore") as file:
        for i in range(500):
            file.write(scores[i] +"\n")
    print("suffixscores.txt was created")

    with open("topsuffixnoscore.txt","w", errors="ignore") as file:
        for i in range(0, 500):
            top = scores[i].split()
            if top != []:
                print(top)
                file.write(top[1] +"\n")
        print("topsuffixnoscore.txt was created")
    print("topsuffixnoscore.txt was created")
    #for com in scores:
    
    #    print(com)
    #to print results without score
    #for com in scores:
    #    com = com.split()
    #    print(com[1])