class MP:
    def __init__(self,name,age,designation,constituency,driver,totalSpendings):
        self.name = name
        self.age = age
        self.designation = designation
        self.constituency = constituency
        self.driver = driver
        self.totalSpendings = totalSpendings
    
    def getConstituency(self):
        return self.constituency
    
    def getDriver(self):
        return self.driver
    
    def isLiableToBeArrested(self,totalSpendings):
        return totalSpendings > 100000
    

class Minister(MP):
    def __init__(self,name,age,designation,constituency,driver,totalSpendings):
        super().__init__(name,age,designation,constituency,driver,totalSpendings)
    
    def isLiableToBeArrested(self,totalSpendings):
        return totalSpendings > 1000000
    

class PM(Minister):
    def __init__(self,name,age,designation,constituency,driver,totalSpendings,permissionToArrestMinister):
        self.permissionToArrestMinister = permissionToArrestMinister
        super().__init__(name,age,designation,constituency,driver,totalSpendings)

    def isLiableToBeArrested(self,totalSpendings):
        return (totalSpendings > 10000000 and self.permissionToArrestMinister) 
    

class Commissioner:
    def __init__(self,name,age,designation):
        self.name = name
        self.age = age
        self.designation = designation

    def willArrest(self,ministerObj,pmObj):
        if(ministerObj.designation == "PM"):
            print("PM can't be arrested !")
        if pmObj.permissionToArrestMinister == 0:
            print("Permission is not granted by the PM to arrest Minister ! ")
        elif ministerObj.isLiableToBeArrested(ministerObj.totalSpendings):
                
                amount = 0
                if ministerObj.designation == "Minister":
                    amount = 1000000
                elif ministerObj.designation == "MP":
                    amount = 100000
                print(f"{ministerObj.name} will be arrested as he/she is a {ministerObj.designation} and the total spendings ({ministerObj.totalSpendings}) exceeds the amount {amount}")

                    
c = Commissioner("Prasanna",50,"Commissioner")
pm1 = PM("Modi",70,"PM","UP","umesh",1530434,1)
m1 = Minister("Amit",56,"Minister","Delhi","daya",110340524)


c.willArrest(pm1,pm1)    
c.willArrest(m1,pm1)

    

    




    
