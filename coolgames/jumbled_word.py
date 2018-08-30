import random;
def choose():
    lst=["mathematics","letusc","player","football","jobinterview"]
    pick=random.choice(lst)
    return pick;
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled;
def thank(p1,p2,point1,point2):
    print("Thank you for joining the game",p1,p2);
    print(p1,"your score is",point1);
    print(p2,"your score is ",point2);
    if point1==point2:
        print("So here you can see you are drawn");
    elif point1>point2:
        print("Now it is time to congratualte our winner",p1)
    else:
        print("Now it is time to congratulate our winner",p2)
def play():
    p1name= input("player 1,please enter your name")
    p2name= input("player 2, please enter your name");
    pp1=0
    pp2=0
    turn= 0
    while(1):
        picked_word = choose()
        qn=jumble(picked_word);
        print(qn);
        print(turn);
        if turn%2==0:
            print(p1name,"your turn")
            ans=input("what is on my mind")
            if ans==picked_word:
                pp1=pp1+1
                print("your score is",pp1);
            else:
                print("Better luck next time")
            c=input("press 1 to continue and 0 to quit")
            if c=='0':
                thank(p1name,p2name,pp1,pp2);
                break;
            else:
                turn=turn+1;
            #player2
        else:
            print(p2name, "your turn")
            ans = input("what is on my mind")
            if ans == picked_word:
                pp2 = pp2 + 1
                print("your score is", pp2);
            else:
                print("Better luck next time")
            c = input("press 1 to continue and 0 to quit")
            if c == '0':
                thank(p1name, p2name, pp1, pp2);
                break;
            else:
                turn = turn+1;
play();