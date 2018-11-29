import sys
import os
import csv
import got3 as got


def dateForm(yy, mm, dd):
    
    _str = str(yy) +"-" + str(mm).zfill(2) + "-"+ str(dd).zfill(2)
    
    return _str

def main():

    
    getCnt = 30                             #setting the number that you want to retrieve
    keyWord = "Golden State Warriors"       #Key Word
    year = 2016                             #Start Date
    month = 12
    day = 10
    print("--- Start scraping {} ---".format(keyWord))
    while(True):
        
        #End Date
        if(year==2016 and month==12 and day==13):
            break
    
        startDate = dateForm(year, month, day)
        
        day = day+1
        
        if(day == 32):
            day = 1
            month +=1
            
        if(month == 13):
            month = 1
            year +=1
        
        endDate = dateForm(year, month, day)
        
        
        # make folder
        csvFilePath = keyWord + "_" + startDate[0:len(startDate)-3]
        if not os.path.exists(csvFilePath):
            print(csvFilePath)
            os.makedirs(csvFilePath)

        # get tweets
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keyWord).setSince(startDate).setUntil(endDate).setMaxTweets(getCnt).setLang("en")    

        tweets = got.manager.TweetManager.getTweets(tweetCriteria)

        
        # write to cvs
        fileName = csvFilePath +"/"+ keyWord + "_" + startDate +".csv"
        print(fileName)
        with open(fileName, 'w') as csvfile:
            
            fieldnames = ['text', 'date', 'id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for tweet in tweets:
                testdict ={ }
                testdict['text'] = tweet.text
                testdict['date'] = tweet.date
                testdict['id'] = tweet.id

                writer.writerow(testdict)
    



if __name__ == '__main__':
    main()
    print("--- End ---")

