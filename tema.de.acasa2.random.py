from random import randint 
def loto():
    puncte=0
    numar=0
    lst=[]
    lista1=[]
    for i in range(0,10):
        for k in range(0,5):
            numar = randint(0,36)
            while numar in lst:
                numar = randint(0,36)
            lst.append(numar)
        for m in range(0,5):
            numar = randint(0,36)
            while numar in lista1:
                numar = randint(0,36)
            lista1.append(numar)
        print("Numerele voastre sunt: ",lista1)
        print(i+1,"Varianta este:",lst)
        for n in lista1:
            if n in lst:
                puncte+=1
        if(puncte==5):
            print("Jackpot")
        elif(puncte==4):
            print("locul 2!")
        elif(puncte==3):
            print("locul 3!")
        else:
            print("zero castig:(")
        print("\n")
        lst=[]
        lista1=[]
        puncte=0
loto()