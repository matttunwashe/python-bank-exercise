#creates empty list at the start of the program
cusnames=[]
cuspasswords=[]
cusbalance=[]

#opens storage file to save old customer data
namefile=open("cusnamefile.txt", "r")
passfile=open("cuspassfile.txt", "r")
balfile=open("cusbalfile.txt", "r")

#store the empty lists with data from storage files
#list of customer names
for line in namefile:
    cusnames.append(line[:-1])
namefile.close

#list of customer passwords
for line in passfile:
    cuspassfile.append(line[:-1])
passfile.close()

#list of customer balance
for line in balfile:
    cusbalfile.txt(line[:-1])
balfile.close()


#creates a new user
def cusaccountcheck():
    name=""
    pin=""

    while name not in cusnames and len(name):
        name=input("Type your name for this new ban account\n")
        if name not in cusnames:
            cusnames.append(name)
            filewrite(cusnames)
            break
        print ("Sorry that user name is already in use")
        ans=raw_input("Are you an existing customer? (y/n)\n")
        if ans.lower()=="y":
            olduscheck()
        else:
            cusaccountcheck()

    while len(pin)<4:
        pin=input("Please assign a password to this account, pin should be at least 5 characters\n")
        if len(pin)>4:
            print ("your pin has been successfully saved")
            print ("don't disclose your pin to anyone")
            cuspasswords.append(pin)
            cusbalance.append(0)
            balance=100.0
            cusbalance[cusnames.index(name)]=balance
            filewrite(cuspasswords)
            filewrite(cusbalance)
            break
        print("Sorry, that is a short password")

    return name,pin, balance

#function to check returning customer
def oldcuscheck():
    name=""
    while name not in cusnames:
        name=raw_input("What is your name?\n")
        if name in cusnames:
            username=name
            userpassword=cuspasswords[cusnames.index(name)]
            balance=float(cusbalance[cusnames.index(name)])
            return username, userpassword, balance
        else:
            print("Sorry %s, Name not in records, Please type in your name corredctly"%names)
            again=raw_inout("Type in your name again? (y/n)")
            if again.lower()== "y":
                olducheck()
            else:
                print ("Bye, Thanks for using PostBank")
                exit()
#Writes information in the files when needed
def filewrite(item):
    if item==cusnames:
        text=open("cusnamefile.txt","w")
        for i in item:
                text.write(i+"\n")
        text.close()
    elif item==cuspasswords:
        text=open("cuspassfile.txt", "w")
        for i in item:
                text.write(i+"\n")
        text.close()
    elif item==cusbalance:
        text=open("cusbalfile.txt", "w")
        for i in item:
                text.write(str(i)+"\n")
        text.close()

#Updates the account after a deposit or withdrawal
def balupdate(ind, amount):
    accountnumber=cusnames.index(ind)
    accountbal=float(cusbalance[accountnumber])
    accountbal+=amount
    cusbalance[accountnumber]=accountbal
    text=open("cusbalfile.txt", "w")
    for i in cusbalance:
            text.write(str(i)+"\n")
    text.close()

#Deletes existing account and all its data
def deleteaccount(name):
    accountnumber=cusnames.index(name)
    del cusnames[accountnumber]
    filewrite(cusnames)
    del cusbalance[accountnumber]
    filewrite(cusbalance)
    del cuspasswords[accountnumber]
    filewrite(cuspasswords)
    return None

    
                

    

    
        
        
            



                    
