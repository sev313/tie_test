import pandas as pd
import os


class Actuator():
    
    def __init__(self, selfcurrent):
        self.current = 0
        self.state = ""
        self.config = os.path.join(os.getcwd(), "actuator", "config", "currentVsPosition 1.xlsx")
        self.table = self.PopulateTable()
        
        self.lowerLimit = 0
        self.upperLimit = self.table.iloc[-1]["current"]
        
        self.Initialize()
        
        
        
    #--------------Helper Methods ---------------------
    def PopulateTable(self):
        df = pd.read_excel(self.config)
        return df
    
    def ErrorMsg (self):
        
        print ("The actuator is in an error state")
        
    def LookupPosition(self):
        
        #print ("current:", self.current  )
        for i in range(self.table.shape[0]):
            
            if self.table.iloc[i]["current"] == self.current:
                return self.table.iloc[i]["position"]
            elif self.table.iloc[i]["current"] > self.current:
                if i>0:
                    return self.table.iloc[i-1]["position"]
                else:
                    return self.table.iloc[0]["position"]
    
    
    #-------------Main Class Methods---------------------
        
    def Initialize(self):
        #Prepare the actuator for operation.
        self.state = "Uninitialized"
        
    def SetCurrent(self, current):
        #Set the actuator current
        
        if self.state == "Error":
            self.ErrorMsg()
        else:
            
        
            if current <= self.upperLimit and current >0:
                
                self.current = current
                self.state = "Operational"
            else:
                
                self.state = "Error"
                
        
    def GetPosition (self):
        #Return the current state of the actuator
        
        if self.state == "Error":
            self.ErrorMsg()
            return None
        
        else:
            return self.LookupPosition()
            

            
    def GetState(self):
        #The state is returned even when there's an error
        return self.state
    
        
    def Shutdown(self):
        self.state = "Uninitialized"
        self.current = 0
        
        
        
        
        