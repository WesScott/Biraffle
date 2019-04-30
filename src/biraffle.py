import csv
import random
from random import shuffle

entryList = []
pickList = []

class Entry:
    Name: None
    Points: 0
    UserID: None

    def setName(self,name):
        self.Name = name
    def getName(self):
        return self.Name

    def addPoint(self):
        self.Points += 1
    def setPoints(self,points):
        self.Points = points
    def getPoints(self):
        return int(self.Points)

    def setID(self, userid):
        self.UserID = userid
    def getID(self):
        return self.UserID

    def printEntry(self):
        print("Name: " + self.getName())
        print("Points: {}".format(self.getPoints()))
        print("ID: " + self.getID() + "\n")

def createEntry():
    entry = Entry()
    entry.setName(input("Please enter name"))
    entry.setPoints(input("Please enter points"))
    entry.setID(input("Please enter ID"))
    entryList.append(entry)

def createEntry(name, points, userid):
    entry = Entry()
    entry.setName(name)
    entry.setPoints(points)
    entry.setID(userid)
    entryList.append(entry)

def printEntries():
    for entry in entryList:
        entry.printEntry()

def clearEntries():
    entryList.clear()

def clearPicks():
    pickList.clear()

def shufflePicks():
    shuffle(pickList)

def populatePicks():
    for entry in entryList:
        for i in range(0,(entry.getPoints())):
            pickList.append(entry)

def printPicks():
    for entry in pickList:
        entry.printEntry()

def pickWinner():
    num = random.randint(0,len(pickList)-1)
    pickList[num].printEntry()

def startRaffle():
    populatePicks()
    shufflePicks()
    print("\nAnd the winner is:")
    pickWinner()

#"""
with open('entries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("Columns: {}".format(", ".join(row)))
            line_count += 1
        else:
            #print('\t{} has {} points, and their user ID is {}.'.format(row[0],row[1],row[2]))
            createEntry(row[0],row[1],row[2])
            line_count+=1
        print("Processed {} users (not including duplicates)".format(line_count))
    while(True):
        choice = input("Press Enter to draw a winner, Type 'quit' to exit.")
        if choice == "quit":
            break
        else:   
            startRaffle()
#"""    
                  
            
