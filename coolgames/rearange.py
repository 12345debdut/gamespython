import random;
print("HEY WE ARE GOING TO PLAY REARANGE GAME");
choice=int(input("IF YOU HAVE INTEREST ENTER 1 OR ELSE 0"));
def randomword(word):
    r = "";
    l=[];
    c=0;
    while(c!=len(word)):
        y=random.randint(0,len(word));
        if y in l:
            print("hii");
        else:
            l.append(y);
            c+=1
            r=r+word[y];
    print(r);
def questiongen():
    lst= ["print","profile","answers","google","gesture"];
    x=random.randint(0,5);
    choose= lst[x];
    randomword(choose);

if choice==1:
    print("you are in our game now let's start our game");
    questiongen();
    #print("our first question",question);
else:
    print("BETTER LUCK NEXT TIME");