import sys


# from tempLib import *
# import time
#
# tcp255=Tcp("10.179.247.153",255)
#
# sys.stdout = open('log1', 'w')
# while True:
#     time.sleep(.02)
#     tcp255.ULP_Get_Current_Time(21,1,0,0)
#     time.sleep(.02)
#     tcp255.ULP_Get_Component_Information(21,0,0,0,0)
#     time.sleep(.02)
#     tcp255.Nova_BU_Get_Close_Inhibition_By_Wire_Enabling(1,0,0)



from PyIMULibrary.PyIMU import *
tcp255=MBTCP("10.179.247.153",255)
import datetime
logtime=  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
tcp255.Establish_Connection()

sys.stdout = open('log1', 'w')
print logtime
while True:
    # try:
        time.sleep(2)
        tcp255.ULP_Get_Current_Time(21,1,0,0)
        time.sleep(2)
        tcp255.ULP_Get_Component_Information(21,0,0,0,0)
        time.sleep(2)
        tcp255.Nova_BU_Get_Close_Inhibition_By_Wire_Enabling(1,0,0)
    # except:
    	break

tcp255.Disestablish_Connection()
