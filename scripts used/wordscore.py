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
        if wordtrends.count(password[0:-4]) == 0 and len(password[0:-4]) > 5:
            wordtrends.append(password[0:-4])

        if wordtrends.count(password) == 0 and len(password) > 5:
            wordtrends.append(password)

        wordcount = wordcount + password + " "

    for score in wordtrends:
        scores.append(str(wordcount.count(score))  + " " + score)
        
    scores.sort(key=func, reverse=True)

    with open("wordscores.txt","w", errors="ignore") as file:
        for i in range(500):
            file.write(scores[i] +"\n")
    print("wordscores.txt was created")

    with open("topwordswithoutscores.txt","w", errors="ignore") as file:
        for i in range(0, 500):
            top = scores[i].split()
            if top != []:
                print(top)
                file.write(top[1] +"\n")
    print("topwordswithoutscores.txt was created")
    #for com in scores:
    
    #    print(com)
    #to print results without score
    #for com in scores:
    #    com = com.split()
    #    print(com[1])