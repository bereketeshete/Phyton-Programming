balance = 0

def bank():
    while True
    func = str(raw_input("What do you want to do? deposit(d)  or withdrawal(w) or balance check(c)  "))
    if func == "":
        return
    elif func == "d":
        deposit = raw_input("How much amount of money do you want to deposit  ")
        global balance
        balance = balance + int(deposit)
        print  "you have deposited "  + str(deposit)  + " won"
    elif func == "w":
        withdrawal = raw_input("How much amount of money do you want to withdraw  ")
        global balance
        if balance - withdrawal <= 0 :
            print "you can only withdraw upto" + str(balance) + "won"
        else:
            balance = balance - withdrawal  
            print "you have withdrawed " + str(withdrawal) + " won"
            
    elif func == "c":
        print balance
    elif func == "":
        return 
  

