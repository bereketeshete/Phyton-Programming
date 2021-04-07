

def deci_to_any(n, radix) : 
    if 2<= int(radix) <=16 and int(n)>0:
        a=int(n)
        b=int(radix)
        c=int(n)
        if a%b>9:
            G=["A","B","C","D","E","F"]
            print str(a)+ " in base 10 is "+ str(a/b)+G[a%b-10] +" in base 16"
        else:
            while a/b !=0:
                x=a%b
                converted.append(x)
                a=a/b
            x=a%b
            converted.append(x)
            a=a/b            
            converted.reverse()
            d=""
            for i in range(len(converted)):
                d=d+str(converted[i])
            print str(c) + " in base 10 is "+str(d) +" in base "+str(radix)
    else:
        print "Wrong input!!!"
while True:
    n = raw_input("Enter integer ")
    radix =  raw_input("Enter radix ")
    converted=[]
    deci_to_any(n, radix)