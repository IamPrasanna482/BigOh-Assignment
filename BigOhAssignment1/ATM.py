import bisect 
# for adding denomination in the sorted denominations list


# create singleton ATM Class
class ATM:
    _instance = None

    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance = super(ATM,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.denominations = [] # maintains the list of denominations type
        self.numberOfDenominations = {}  # maintains the number of denominations
        self.totalMoney = 0  # stores the total money
        self.customers = {}  # maintains the customers
        tcuUnits = {} # stores all the transaction control units with {'name' : 'place'}


# Create TCU Class
class TransactionControlUnits:
    def __init__(self,name,location):
        self.name = name
        self.location = location

    # method to add customer
    def addCustomer(self,custObj,atmObj):
        ac = custObj.accountNumber
        atmObj.customers[ac] = custObj.balance
        print(f"User:{custObj.name} with accountNumber:{ac} is added successfully !")

    # method to add denomination
    def addDenomination(self,atmObject,denomination):
        bisect.insort(atmObject.denominations,denomination)
        if denomination not in atmObject.numberOfDenominations:
            atmObject.numberOfDenominations[denomination] = 0
        
    # method to print denomination
    def printDenominationList(self,atmObject):
        print(f"The current denominations are : {atmObject.denominations}")
    
    # method to remove denomination
    def removeDenomination(self,atmObject,denomination):
        if denomination not in atmObject.denominations:
            print("Denomination to be removed does not exist")
        else:
            atmObject.denominations.remove(denomination)


    # method to print the available balance
    def printAvailableBalance(self,atmObj):
        print(f"The total money is : {atmObj.totalMoney}")
        print("The denominations and quantity is : ")
        print(atmObj.numberOfDenominations)


    # method to add money 
    def addMoney(self,atmObject):
        li = atmObject.denominations
        print(f"Only these denominations are available to be added : {li}")

        ch = input("Select Y/N : ")

        total = 0
        
        if ch=='Y':
            for d in li:
                noOfNotes = int(input(f"Enter number of {d} notes : "))
                total += (d)*(noOfNotes)
                atmObject.numberOfDenominations[d] = noOfNotes
            print(f"Current Available Money is {total} & the denominations are {atmObject.numberOfDenominations} ")
            atmObject.totalMoney = total
        else:
                return 
    
    # method to print the customers
    def printCustomers(self, atmObj):
        print("List of Customers:")
        for account_number, balance in atmObj.customers.items():
            print(f"Account Number: {account_number}, Balance: {balance}")
    
        

# Create Customer class
class Customer:
    def __init__(self,name,age,accountNumber,mobileNo,balance):
        self.name = name
        self.age = age
        self.accountNumber = accountNumber
        self.mobileNo = mobileNo
        self.balance = balance
    
    # method to check balance
    def checkBalance(self,atmObj,ac):
        bal = atmObj.customers[ac]
        print(f"Your current balance is {bal}")
    
    # method to withdraw money
    def withdrawMoney(self,atmObj,money):
        tempMoney = money
        currentBalance = atmObj.totalMoney
        if (currentBalance < money):
            print(f"Insufficient Balance, current balance is {currentBalance}")
        else:
            dic = {}
            tempList = atmObj.denominations[::-1]
            for i in tempList:
                if money%i == 0:
                    noOfNotes = money/i
                    dic[i] = noOfNotes
                    money -= i*noOfNotes
                elif i > money:
                    continue
                else:
                    print(f"Enter amount which is in the multiple of {i}")
            if money==0:
                print(f"Successfully withdrawn {tempMoney} amount & and the denominations are :")
                print(dic)
            print("----------------------------------------------------------------------------")



totalCustomers = {}

# UUID for the admin to check weather original admin is entering or not
tcuUUID = '1234'

tcu = None

# Menu based program 
while True:
    print("Welcome to Bank")
    print("1. TCU Controller")  
    print("2. Customer")  
    print("3. Exit")  
    ch = int(input("Enter your choice"))

    if ch == 1:
        tcuId = (input("Enter the password for TCU "))
        if tcuId == tcuUUID:
            while True:
            # All functionalities of TCU Controller
                print("1. Initialize ATM object")
                print("2. Initialize TCU Control Unit")
                print("3. Add denomination")
                print("4. Remove denomination")
                print("5. Print all denominations")
                print("6. Print available balance")
                print("7. Add Money")
                print("8. Exit")

                ch2 = int(input("Enter your choice"))

                if ch2 == 1:
                    atm1 = ATM()

                elif ch2 == 2:
                        tcuName = input("Enter TCU Name")
                        tcuPlace = input("Enter TCU Place")
                        tcu = TransactionControlUnits(tcuName,tcuPlace)

                elif ch2==3:
                    d = int(input("Enter the denomination"))
                    tcu.addDenomination(atm1,d)
                    print(f"{d} denomination added successfully !")

                elif ch2==4:
                    d = int(input("Enter the denomination to be removed"))
                    tcu.removeDenomination(atm1,d)
                    print(f"{d} denomination removed successfully !")

                elif ch2==5:
                    tcu.printDenominationList(atm1)

                elif ch2==6:
                    tcu.printAvailableBalance(atm1)

                elif ch2==7:
                    tcu.addMoney(atm1)

                elif ch2==8:
                    break

        else:
            print("Authentication failed")
        
    elif ch==2:
        # All functionalities of Customer
        while True:
            print("1. Create & Add customer")
            print("2. Withdraw Money")
            print("3. Print customers")
            print("4. Exit")

            ch3 = int(input("Enter the Choice:"))

            if ch3==1:
                name = input("Enter the name of customer.")
                age = int(input("Enter the age of the customer"))
                accountNumber = int(input("Enter the accountNumber of the customer"))
                mobileNumber = int(input("Enter the mobileNumber of the customer"))
                balance = int(input("Enter the money to be deposited"))
                cust1 = Customer(name,age,accountNumber,mobileNumber,balance)
                tcu.addCustomer(cust1,atm1)
            elif ch3==2:
                m = int(input("Enter the money to be withdrawn"))
                cust1.withdrawMoney(atm1,m)
            elif ch3==3:
                tcu.printCustomers(atm1)
            elif ch3==4:
                break
    elif ch==3:
        break






























        


# atm1 = ATM()
# tcu = TransactionControlUnits("SBI","Ghaziabad")



# tcu.addDenomination(atm1,100)
# tcu.addDenomination(atm1,200)
# tcu.addDenomination(atm1,500)
# tcu.addDenomination(atm1,2000)

# tcu.removeDenomination(atm1,200)



# tcu.addMoney(atm1)

# tcu.printDenominationList(atm1)
# tcu.printAvailableBalance(atm1)

# cust1 = Customer("Prasanna",22,1432,8920481981)
# cust2 = Customer("Prasoon",23,9837,2312093822)

# tcu.addCustomer(cust1,atm1,1432)


# cust1.checkBalance(atm1,1432)
# cust1.withdrawMoney(atm1,2000)

# tcu.addCustomer(cust2,atm1,9837)


# tcu.addCustomer(cust1,atm1,23)
# cust1.checkBalance(atm1,1432)
# tcu.addDenomination(atm1,100)
# tcu.addDenomination(atm1,200)
# tcu.addDenomination(atm1,500)
# tcu.addDenomination(atm1,1000)

# tcu.printAvailableBalance(atm1)
# print(tcu.printDenominationList(atm1))

# tcu.addMoney(atm1)

# tcu.withdrawMoney(atm1,1234)

# tcu.removeDenomination(c1,5)

# print(tcu.printDenominationList(c1))











# while True:
#     print("Welcome to Bank")  
#     print("1. Add denomination")  
#     print("2. Remove denomination")  
#     print("3. Print denomination")  
#     print("4. Print available balance")  
#     print("5. Create customer")  
#     print("6. Print customers")  
#     print("7. Withdraw Balance")  
#     print("8. Exit")  

#     ch = int(input("Enter the Choice:"))



#     if ch == 1:
#         d = int(input("Enter the denomination"))
#         tcu.addDenomination(atm1,d)
#         print(f"{d} denomination added successfully !")

#     elif ch==2:
#         d = int(input("Enter the denomination to be removed"))
#         tcu.removeDenomination(atm1,d)
#         print(f"{d} denomination removed successfully !")

#     elif ch==3:
#         tcu.printDenominationList(atm1)

#     elif ch==4:
#         tcu.printAvailableBalance(atm1)


#     elif ch==5:
#         name = input("Enter the name of customer.")
#         age = int(input("Enter the age of the customer"))
#         accountNumber = int(input("Enter the accountNumber of the customer"))
#         mobileNumber = int(input("Enter the mobileNumber of the customer"))
#         # print(Customer(name,age,accountNumber,mobileNumber))
#         totalCustomers[id] = Customer(name,age,accountNumber,mobileNumber)
#         id += 1
#         # tcu.addCustomer(name,age,accountNumber,mobileNumber)

#     elif ch==6:
#         print(totalCustomers)

    




# tcu.addDenomination(atm1,100)
# tcu.addDenomination(atm1,200)
# tcu.addDenomination(atm1,500)
# tcu.addDenomination(atm1,2000)

# tcu.addMoney(atm1)

# cust1 = Customer("Prasanna",22,1432,8920481981)
# cust2 = Customer("Prasoon",23,9837,2312093822)

# tcu.addCustomer(cust1,atm1,1432)


# cust1.checkBalance(atm1,1432)
# cust1.withdrawMoney(atm1,2000)

# tcu.addCustomer(cust2,atm1,9837)


# # tcu.addCustomer(cust1,atm1,23)
# # cust1.checkBalance(atm1,1432)
# # tcu.addDenomination(atm1,100)
# # tcu.addDenomination(atm1,200)
# # tcu.addDenomination(atm1,500)
# # tcu.addDenomination(atm1,1000)

# # tcu.printAvailableBalance(atm1)
# # print(tcu.printDenominationList(atm1))

# # tcu.addMoney(atm1)

# # tcu.withdrawMoney(atm1,1234)

# # tcu.removeDenomination(c1,5)

# # print(tcu.printDenominationList(c1))

