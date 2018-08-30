x=int(input("enter the lower bound"));
y=int(input("enter the upper bound"));
for i in range(x,y+1):
    if(i%15==0):
        print("FIZZBUZZ",i);
        continue;
    if(i%3==0):
        print("FIZZ",i);
        continue;
    if(i%5==0):
        print("BUZZ",i);
        continue;
    else:
        print(i);