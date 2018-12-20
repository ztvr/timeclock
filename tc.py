from time import strftime
import time
import sys
import os.path
### MAKE TIMECARD A SQLITE DB ###
#import sqlite3

#Timeclock Mode Dictionary
modes = {
    "timeIn": 1,
    "timeOut": 2,
    "reportWeek": 3,
    "reportDay": 4,
    "editLast": 5
}

#Timecard Location
timecard = "C:\\Users\\jreesez\\Documents\\#Apps\\TimeClock\\timecard.txt"

def printGreeting():
    #Print Greeting
    print("Welcome to ZvR TimeClock", end='', flush=True)

    #Dramatic Ellipses
    i = 3
    while i > 0:
        print('.', end='', flush=True)
        time.sleep(0.5)
        i -= 1

def printGoodbye():
    #Print Goodbye
	print("Thank you for using ZvR TimeClock, Goodbye!")
	
def printHelpMenu():
    global modes
    print("\n\tAvailable modes are:")
    for i in sorted(modes.keys()):
        #print("\t",modes)
        print("\t\t", i)
        
def switchMode(startupArgs):
    global modes
    if len(startupArgs) <= 1 or len(startupArgs) > 2:
        printHelpMenu()
        exit()
    else:
        return modes.get(str(startupArgs[1]), "Invalid Mode!")

def logAccess(timeCardFile, accessTime):
    f = open(timeCardFile, 'a')
    logEntry = "Time Card Accessed on " + accessTime + ".  Mode was: " + str(mode) +".\n"
    f.write(logEntry)
    f.close()
    print("Time Logged.")
	
#Main Execution
printGreeting()
mode = switchMode(sys.argv)
print("\nMode Number: ", mode, ": ", str(sys.argv[1]))
logAccess(os.path.abspath(timecard), strftime("%m/%d/%Y %I:%M:%S %p"))
printGoodbye()