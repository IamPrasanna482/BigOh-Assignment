# PCU, GTI, Regalia are solar Inverters
# Zelio, iCruze are nonSolar Inverters


class Inverter:
    def __init__(self, name, current, voltage):
        self.name = name
        self.current = current
        self.voltage = voltage
    def getPowerRating(self):
        return (self.current)*(self.voltage)
        


class SolarInverter(Inverter):
    def __init__(self, name, current, voltage, hasBattery, hasGridOn):
        self.hasBattery = hasBattery # True/False
        self.hasGridOn = hasGridOn # True/False
        super().__init__(name, current,voltage)
    
        
    def getInfo(self):
         return (f"{self.name} is SolarInverter, runs on : {self.current} Amp, {self.voltage} Volts, hasBattery = {self.hasBattery}, hasGridOn = {self.hasGridOn} and the PowerRating is {self.getPowerRating()}\n")
        
class NonSolarInverter(Inverter):
    def __init__(self,name, current, voltage, hasBattery):
        self.hasBattery = hasBattery
        super().__init__(name,current,voltage)
        
        
    def getInfo(self):
        return (f"{self.name} is nonSolarInverter, runs on : {self.current} Amp, {self.voltage} Volts, hasBattery = {self.hasBattery} and the PowerRating is {self.getPowerRating()}\n")

PCU = SolarInverter("PCU",12,220,True,False)
GTI = SolarInverter("GTI",8,240,False,True)
Regalia = SolarInverter("Regalia",10,220,True,True)

Zelio = NonSolarInverter("Zelio",15,220,True)
iCruze = NonSolarInverter("iCruze",20,240,True)


# SolarInverter
print(PCU.getInfo())
print(GTI.getInfo())
print(Regalia.getInfo())

#NonSolarInverter
print(Zelio.getInfo())
print(iCruze.getInfo())




    


# class NonSolarInverter(Inverter):
#     def __init__(self,current,voltage,haveBattery)


    
    
     
     