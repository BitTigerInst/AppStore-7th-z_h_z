from pymongo import MongoClient
import datetime
from datetime import date
from time import strptime
class DataService(object): 
    @classmethod
    def init(cls,client):
        cls.client=client
        cls.db=client.appstore
        cls.appinfo=cls.db.appInfo
        
    @classmethod
    def retrieve_ratings(cls,filter_dict={}):
        rating={};
        dates={};
        rates={};
        cursor=cls.db.appInfo.find({"allRating":{'$exists':True}})
        for appInfo in cursor:
            appID=str(appInfo['appID'])
            dates[appID]=str(appInfo['lauch_time']).replace('[','').replace(']','').replace("u'",'').replace("'",'')
            rating[appID]=str(appInfo['allRating']).split(", ")[0].split(" ")[0].replace('[','').replace(']','').replace("u",'').replace("'",'')
            rates[appID]=str(appInfo['allRating'].split(", ")[1].split(" ")[0])
           # .split[" Ratings"][0]
            #try:
            #   appInfo['allRating']
            #except NameError:
            #    rates[appInfo['appID']]=None
            #else:
            #    rates[appInfo['appID']]=appInfo['allRating'].split(", ")[1]
        #result={rating,date,rates}
        return (rating,dates,rates)

def main():
    try:
        client=MongoClient('localhost',27017)
        DataService.init(client)
        rating,dates,rates=DataService.retrieve_ratings()
        popular(rating,dates,rates)
        #print date
    except Exception as e:
        print(e)
        print('haha')
    #finally:
    #    if 'client' in locals:
    #        client.close()
def popular(rating,dates,rates):
    score={}
    for appID in rating:
        #print rating[appID]
        r=float(rating[appID])
        year=int(dates[appID].split(', ')[1])
        month=dates[appID].split(', ')[0].split(' ')[0]
        rmonth=strptime(month,'%b').tm_mon
        day=int(dates[appID].split(', ')[0].split(' ')[1])
        today = date.today()
        someday = date(year, rmonth, day)
        diff=(today-someday).days
        print diff
        num=int(rates[appID])
        score[appID]=num/diff*r
        
        
        

        
if __name__=="__main__":
    main();
