import pandas as pd

from actuator.actuator import Actuator


# Example use case

#Init
ac1 = Actuator(0)

#Set Current
ac1.SetCurrent(1)

#Get Position
print (ac1.GetPosition())

#Get State
print (ac1.GetState())


#Shutdown
ac1.Shutdown()
