from enum import Enum
import numpy as np


# Enum for vehicle types to increase code reusability
class Vehicle(Enum):
    BIKE = 1
    TRUCK = 2
    CAR = 3
    VAN = 4
    ELECTRICCAR = 5


# Enum for vehicleParkingType to increase code reusability
class VehicleParkingType(Enum):
    COMPACT = 0
    LARGE = 1
    HANDICAPPED = 2
    BIKE = 3

# Initialize class User that acts as a base class for admin, customer and attendant to initialize name, age, mobileNo and the role
class User:
    def __init__(self, name, age, mobileNo, role):
        self.name = name
        self.age = age
        self.role = role
        self.mobileNo = mobileNo


# Initialize class Admin
class Admin(User):
    def __init__(self, name, age, mobileNo, role):
        super().__init__(name, age,mobileNo, role)

# Initialize class Attendant
class Attendant(User):
    def __init__(self, name, age, mobileNo, role):
        super().__init__(name, age, mobileNo, role)
 
    #calculate totalPrice of the customer parking for the duration of (exitTime)-(entryTime)
    def calculateTotalPrice(self, customerObj, exitTime):

        totalTime = exitTime - customerObj.entryTime
        totalPrice = 0

        # customers have to pay $4 for the first hour, $3.5 for the second and third hours, and $2.5 for all the remaining hours.

        if totalTime > 3:
            totalPrice = 11
            totalTime -= 3
            totalPrice += (totalTime)*2.5
        elif totalTime == 3:
            totalPrice = 11
        elif totalTime == 2:
            totalPrice = 7.5
        elif totalTime == 1:
            totalPrice = 4
        customerObj.totalPrice = totalPrice

        

        print(f"Total price is ${totalPrice} for the parking duration of {totalTime} Hours")
     
     # takePayment method 
    def takePayment(self,customerObj):
        if customerObj.modeOfPayment == 0:
            # cash payment
            print(f"Cash Amount is successfully taken")
        else:
            #online payment
            print(f"Online Payment is successfully taken")



# Initialize class Customer
class Customer(User):
    def __init__(self, name, age, role, mobileNo, entryTime, modeOfPayment):
        super().__init__(name, age, mobileNo, role)
        self.entryTime = entryTime
        self.modeOfPayment = modeOfPayment
        print("--------------------------------------------------------------------------------------------")
        print(f"{self.name} customerObject has been created successfully ! ")

    CustSlotNum = 0
    CustFloorNum = 0
    def parkVehicle(self, parkingObj, vehicleType):

        # print(parkingObj.parkingArr)

        floorNumber = Vehicle[vehicleType].value
        # self.CustFloorNum = floorNumber


        # slot = -1

        # for i in range(0,len(parkingObj.parkingArr[floorNumber])):
        #     if parkingObj.parkingArr[floorNumber][i] == 0:
        #         slot = i 

        #         parkingObj.parkingArr[floorNumber][i] = 1
        #         print(parkingObj.parkingArr[floorNumber])
        #         print(f"floor num : {floorNumber} & slot : {i}")
        #         break

        slotNumber = -1
        # print(f"asdf : {len(parkingObj.parkingArr[floorNumber])}")
        for i in range(0,len(parkingObj.parkingArr[floorNumber])):

            if parkingObj.parkingArr[floorNumber][i] == 0:
                slotNumber = i
                break
        
        if slotNumber == -1:
            print(f"Parking for {vehicleType} is full.")
        elif slotNumber is not len(parkingObj.parkingArr[floorNumber]):
            # print(f"debug : {floorNumber} , {slotNumber}")
            parkingObj.parkingArr[floorNumber][slotNumber] = 1
            
            print(f'{vehicleType} is successfully parked at floorNumber : {floorNumber} and slotNumber : {slotNumber}')
            # print(parkingObj.parkingArr[floorNumber])

            # print(parkingObj.parkingArr)
        self.custSlotNum = slotNumber
    

    #removeVehicle method to remove the car form the parking and free the slot
    def removeVehicle(self,parkingObj,vehicleType):
        parkingObj.parkingArr[self.CustFloorNum][self.custSlotNum] = 0
        print(f"{vehicleType} is removed successfully from floor : {self.CustFloorNum} & slot : {self.custSlotNum} & payment is done !")
        print("--------------------------------------------------------------------------------------------")



    def setEntryTime(self, entryTime):
        self.entryTime = entryTime
    



# defining singleton class for ParkingLot ( only one instance is made and used throughout the program )
class ParkingLot:
    _instance = None

    def __new__(cls,size,floors,admin,*args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ParkingLot,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    
    # constructor to initialize the size and floors of the parking slot
    def __init__(self,size,floors,admin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.size = size
        self.floors = floors
        self.parkingArr = [[0]*size]*floors # make a parking list
        

        print(self.parkingArr)
    
        self.admin = admin

    # method to add a new floor
    def addNewFloor(self,size,admin):
        new_row =[0]*size
        self.parkingArr.append(new_row)
        print(f"Floor Number : {size} is successfully created !")

    
    # method to remove a particular floor
    def removeFloor(self,rowNum,admin):
        # print(print(self.parkingArr))
        self.parkingArr.pop(rowNum)
        print(f"Floor Number : {rowNum} is removed successfully !")

    # method to add a new slot
    def addNewSlot(self,floor,admin):
        self.parkingArr[floor].append(0)
        print(f"Slot Number : {len(self.parkingArr[floor])} is successfully created !")

    # method to remove a particular slot
    def removeSlot(self,rowNum,admin):
        # print(print(self.parkingArr))
        self.parkingArr[rowNum].pop()
        print(f"Slot Number : {len(self.parkingArr[rowNum])} is removed successfully !")





class Display:
    @staticmethod
    def isParkingSlotFull(parkingObj, vehicleType):
        floorNum = Vehicle[vehicleType].value
        isAvailable = 1
        for i in parkingObj.parkingArr[floorNum]:
            if i is 0:
                isAvailable = 0


        if isAvailable==0:
            print(f"You can park your {vehicleType}")
        else:
            print(f"Parking floor for {vehicleType} is Full !")



        # if parkingObj.parkingArr[floorNum][1] == parkingObj.size:
        #     print(f"Parking floor for {vehicleType} is Full !")
        # else:
        #     print(f"You can park your {vehicleType}")
    
    # @staticmethod
    # def printParking(parkingObj):
        # print(np.matrix(parkingObj.parkingArr))



def main():
    pass
    # admin = Admin("Prasanna", 23, 9283423948, "admin") # (name, age, mobileNo, role)
    # parking = ParkingLot(5, 5, admin)  # (size,floors,adminObject) ,singleton class
    # attendant = Attendant("John", 30,928123111, "attendant") #(name,age,mobileNo,role)
    # d = Display()
  

    # customer1 = Customer("Gaurav", 34, 3274182731, "customer", 3,0) # (name, age, mobileNo, entryTime, modeOfPayment)

    # d.isParkingSlotFull(parking,"CAR")
    # customer1.parkVehicle(parking,"BIKE")

    # attendant.calculateTotalPrice(customer1,7)
    # attendant.takePayment(customer1)

    # customer1.removeVehicle(parking,"BIKE")




    # customer2 = Customer("Prasoon", 24, 3274182731, "customer", 8,1) # (name, age, mobileNo, entryTime)
    # customer2.parkVehicle(parking,"BIKE")
    
    # attendant.calculateTotalPrice(customer1,7)
    # attendant.takePayment(customer1)


    # parking.addNewFloor(6,admin)
    # parking.removeFloor(1,admin)

    # parking.addNewSlot(3,admin)
    # parking.addNewSlot(3,admin)

    # parking.removeSlot(4,admin)
    # parking.removeSlot(4,admin)




    # attendant.takePayment(customer2)
    # customer4 = Customer("Prasoasdfon", 24, 3274182731, "customer", 3) # (name, age, mobileNo, entryTime)
    # customer5 = Customer("Pragyan", 24, 3274182731, "customer", 3) # (name, age, mobileNo, entryTime)
    # customer6 = Customer("Prakhar", 24, 3274182731, "customer", 3) # (name, age, mobileNo, entryTime)
    # customer7 = Customer("Parth", 24, 3274182731, "customer", 3) # (name, age, mobileNo, entryTime)
    
    # customer1.parkVehicle(parking, "VAN")  
    # customer2.parkVehicle(parking, "BIKE") 
    # customer2 = Customer("Ishaan", 24, 3274182731, "customer", 4,1) # (name, age, mobileNo, entryTime, modeOfPayment)
    # customer2.parkVehicle(parking, "CAR") 
    # customer1.removeVehicle(parking,"VAN")

    # customer3.parkVehicle(parking, "BIKE")  
    # customer4.parkVehicle(parking, "BIKE")  
    # customer5.parkVehicle(parking, "BIKE")  
    # customer6.parkVehicle(parking, "BIKE")  
    # customer7.parkVehicle(parking, "TRUCK")  
    


    # display.printParking(parking)




    # display.isParkingSlotFull(parking, "BIKE")
    # display.VehicleAdded()

    # parking.addNewFloor(8,admin1)
    # # parking.removeFloor(,admin1)

    # attendant.calculateTotalPrice(customer1,7)  # (customerObject, exitTime)

if __name__ == "__main__":
    main()

