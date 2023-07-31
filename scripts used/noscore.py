with open('prefixscores.txt',  errors="ignore") as f:
    count = 0
    scores = f.readlines()
    with open("topprefix.txt","w", errors="ignore") as file:
        for i in range(0, len(scores)):
            top = scores[i].split()
            if top != []:
                print(top)
                file.write(top[1] +"\n")
        print("topprefix.txt was created")
        #for com in scores: