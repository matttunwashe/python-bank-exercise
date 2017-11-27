import filestore
import time
import datetime

def postbank():
    print ("Welcome to the Bank\n")
    prompt = int(input("""To open a new bank account, press 1\n"""+
                            """To access your existing account and transaction press 2\n"""))
    if prompt == 1:
        cus = BankAccount()
        #creates a new customer profile
    elif prompt == 2:
            cus = ReturnCustomer()
            #checks for existing customer
    else:
         print ("Error. Please try again")
         postbank()
#########################################################

#creating an instance for a new bank account and default bank functions
class BankAccount:
    """Class for a bank account"""
    type = "Normal Account"
    def __init__(self):
        #calls function in the module filestore
        self.username, self.userpassword, self.balance=filestore.cusaccountcheck()
        print ("Thank you %s, your account is set up and ready to use \n a 100 pounds has been credited to your account" %self.username)
        time.sleep(2)
        self.userfunctions()


    def userfunctions(self):
        print("\n\n To access any function below, enter the corresponding key")
        print(""" To :
check balance, press B.
deposit cash, press D.
withdraw cash, press W.
Delete account, press D.
exit service, press E\n
:""")
        ans=raw_input("").lower()
        if ans=='b':
            #passcheck functions confirms stored password with user input
            self.passcheck()
            self.checkbalance()
        elif ans=='d':
            self.passcheck()
            self.depositcash()
        elif ans=='w':
            self.passcheck()
            self.withdrawcash()
        elif ans=='x':
            print ("%s, your account is being deleted"%self.username)
            time.sleep(1)
            print("Loading")
            time.sleep(1)
            filestore.deleteaccount(self.username)
            print ("Your account has been deleted, goodbye")
        elif ans=="e":
            print("Thank you for using PostBank services")
            time.sleep(1)
            print ("Goodbye %s" %self.username)
            exit()

        else:
            print ("No function assigned to this key, try again")
            self.functions()
            
        #checking the account balance
        def checkbalance(self):
            date=datetime.date.today()
            date=date.strftime('%d-%B-%Y')
            self.working()
            print ("Your account balance as at {} is {}").format(date, self.balance)
            self.transact_again()


        #withdraw cash functions
        def withdrawcash(self):
            amount=float(raw_input("::\n Enter amount to withdraw\n: "))
            self.balance-=amount
            self.working()
            print ("Your new account balance is %.2f" %self.balance)
            print("::\n")
            filestore.balupdate(self.username, -amount)
            self.transact_again()

        def depositcash(self):
            amount=float(raw_input("::\nPlease enter amount to be deposited\n "))
            self.balance+=amount
            self.working()
            print ("Your new account balance is %.2f" %self.balance)
            print ("::\n")
            filestore.balupdate(self.username, amount)
            self.transact_again()

        def transact_again(self):
            ans=raw_input("Do you want to do another transaction? (y/n)\n").lower()
            self.working()
            if ans=="y":
                self.userfunctions()
            elif ans=="n":
                print ("Thanks for using PostBank. Have a good day")
                time.sleep(1)
                print ("Goodbye {}").format(self.username)
                exit()
            elif ans!="y" and ans!="n":
                print ("Unknown key pressed, choose either 'Y' or 'N'")
                self.transact_again()

        def working(self):
            print ("working"),
            time.sleep(1)
            print("...")
            time.sleep(1)
            print ("..")
            time.sleep(1)
            print(".")
            time.sleep(1)

        def passcheck(self):
            """prompts user for password with every transaction and checks it with stored passwords"""
            b=3
            while b>0:
                ans=raw_input("Type your password to continue with your transaction\n ")
                if ans==self.userpassword:
                    return True

                else:
                    print ("You typed the wrong password")
                    b-=1
                    print ("%d more attempt(s) remaining" %b)

                print ("Account blocked due to three wrong password attempts,\n contact your bank for help, bye!")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print ("..")
                time.sleep(1)
                print(".")

                exit()


class ReturnCustomer(BankAccount):
    type = "Normal Account"
    def __init__(self):
        self.username, self.userpassword, self.balance=filestore.oldcuscheck()
        self.userfunctions()

postbank()
# calling the function to run the program

                        
                
            
            

            

            
        
        
        
