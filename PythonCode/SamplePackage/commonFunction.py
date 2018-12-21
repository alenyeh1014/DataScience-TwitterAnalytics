
# coding: utf-8

# In[1]:


import os
import csv

def date_converter(strDate):
    
    month = month_converter(strDate.split(",")[1].split(" ")[1])

    date = strDate.split(",")[1].split(" ")[2]
    _str = strDate.split(",")[2].strip()                         + "-"+ str(month).zfill(2)                        + "-"+ str(date).zfill(2)
    return _str

def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1


def getGameInfo(teamName):
    # read game result
    gameInfoList =[]
    folderName = "GameResult"
    fileName = teamName
    filePath = os.path.join(os.getcwd(), folderName)
    fileName = os.path.join(filePath, fileName) + ".csv"
    print("Get result from {}".format(fileName))
    file = open(fileName, 'r')
    gameResults = csv.reader(file)
    passHeader = next(gameResults, None)
    for row in gameResults:
        tpTime = int(row[2].split(":")[0])+12
        tpDate = date_converter(row[1])
        gameInfoList.append(GameInfo(row[0], tpDate,tpTime, row[3],row[4]))
        
    return gameInfoList

def getMultipleGameInfo(teamNameLst):
    # read game result
    gameInfoList =[]
    folderName = "GameResult"
    for teamName in teamNameLst:
        fileName = teamName
        filePath = os.path.join(os.getcwd(), folderName)
        fileName = os.path.join(filePath, fileName) + ".csv"
        print("Get result from {}".format(fileName))
        file = open(fileName, 'r')
        gameResults = csv.reader(file)
        passHeader = next(gameResults, None)
        for row in gameResults:
            tpTime = int(row[2].split(":")[0])+12
            tpDate = date_converter(row[1])
            gameInfoList.append(GameInfo(row[0], tpDate,tpTime, row[3],row[4]))
        
    return gameInfoList

def getAllCvsList():
#make cvs list
#ex :.../Blazers_2016-10/Blazers_2016-10-27.csv
    cvslst = []
    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            if name.endswith(".csv"):
                cvslst.append(os.path.join(root,name))
                
    return cvslst

def getCvsPathByGameData(teamName, gameDate):

    cvslst = getAllCvsList()
    matchlist = []
    
    for csvName in cvslst:
        tempName = csvName.split("/")[-1]
        _keyWord = tempName.split("_")[0]
        _csvdate = ""
        if len(tempName.split("_")) > 1:
            _csvdate = tempName.split("_")[1][0:-4]

        #find match file path
        if _keyWord in teamName and _csvdate == gameDate:
            matchlist.append(csvName)
                
    return matchlist

class GameInfo:
    def __init__(self, number, date, time, opponent, result ):
        self.Number = number
        self.Date = date
        self.Time = time
        self.Opponent = opponent
        self.result = result

def sample_func():
    print('Hello!')
