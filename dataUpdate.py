import json
import datetime
from time import strptime
from pymongo import MongoClient


def main():
    dataList = convertData("items.json")
    client = MongoClient()
    db = client.AppStore
    for data in dataList:
        db.appStore.update(
            {"appID": data["appID"]},
            data,
            upsert=True
        )
    return


def calculateDate(date):
    year = int(date.split(',')[1])
    month = date.split(',')[0].split(' ')[0]
    day = int(date.split(',')[0].split(' ')[1])
    rmonth = strptime(month, '%b').tm_mon
    diff = (datetime.datetime.now() - datetime.datetime(year, rmonth, day)).days
    if (diff == 0):
        return 1
    return diff


def calulateRatingValue(rating):
    value = float(rating.split(" ")[0])
    if len(rating.split(" ")) > 2:
        return value + 0.5
    return value


def calPopularRanking(count, rating, diff):
    return count * rating / diff


def calAverageRanking1(currentCount, currentRating, allCount, allRating):
    return currentCount * currentRating * 0.8 + allCount * allRating * 0.2;


def calAverageRanking2(currentCount, currentRating, allCount, allRating, diff):
    if diff <= 3:
        return currentCount * currentRating * 0.9 + allCount * allRating * 0.1;
    elif diff <= 7:
        return currentCount * currentRating * 0.8 + allCount * allRating * 0.2;
    elif diff <= 15:
        return currentCount * currentRating * 0.7 + allCount * allRating * 0.3;
    elif diff <= 30:
        return currentCount * currentRating * 0.6 + allCount * allRating * 0.4;
    else:
        return currentCount * currentRating * 0.5 + allCount * allRating * 0.5;


def convertData(file):
    with open(file, 'r') as data_file:
        json_data = data_file.read()
    dataList = json.loads(json_data)
    for data in dataList:
        data['category'] = data['category'][0].encode('ascii', 'ignore')
        if data.has_key("allRating"):
            data["allRatingValue"] = calulateRatingValue(data["allRating"].split(',')[0])
            data["allRatingCount"] = long(data["allRating"].split(',')[1].split(" ")[1])
        else:
            data["allRatingValue"] = 0.0
            data["allRatingCount"] = 0
        if data.has_key("currentRating"):
            data["currentRatingValue"] = calulateRatingValue(data["currentRating"].split(',')[0])
            data["currentRatingCount"] = long(data["currentRating"].split(',')[1].split(" ")[1])
        else:
            data["currentRatingValue"] = 0.0
            data["currentRatingCount"] = 0
        data['url'] = data['url'][0].encode('ascii', 'ignore')
        data['appID'] = data['appID'].encode('ascii', 'ignore')
        data['lauch_time'] = data['lauch_time'][0].encode('ascii', 'ignore')
        data['diff'] = calculateDate(data['lauch_time'])
        if data['aggregateRating']:
            data['aggregateRating'] = float(data['aggregateRating'][0])
        else:
            data['aggregateRating'] = 0.0
        if data['related_app']:
            for index in xrange(len(data['related_app'])):
                data['related_app'][index] = data['related_app'][index].encode('ascii', 'ignore')
        data["name"] = data["name"][0].encode('ascii', 'ignore')
        data["popularScore"] = calPopularRanking(data["currentRatingCount"], data["aggregateRating"], data["diff"])
        data["averageScore1"] = calAverageRanking1(data["currentRatingCount"], data["currentRatingValue"],
                                                   data["allRatingCount"], data["allRatingValue"])
        data["averageScore2"] = calAverageRanking2(data["currentRatingCount"], data["currentRatingValue"],
                                                   data["allRatingCount"], data["allRatingValue"], data['diff'])
    return dataList


if __name__ == "__main__":
    main();
