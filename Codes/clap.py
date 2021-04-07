
for i in range(1,101,1):
        def funr(i):
                if i<=10 :
                        return i
                else: 
                        return int(i%10)     
        if funr(i) == 4 or funr(i) == 8 :
                print "clap!"
        else:
                print i
        
        