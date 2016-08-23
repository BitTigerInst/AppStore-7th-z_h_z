from pymongo import MongoClient


def main():
    client = MongoClient()
    db = client.AppStore
    # Create Top 1000 Apps for each category
    # categories = db.appStore.distinct("category")
    # for category in categories:
    #     cursor = db.appStore.find({"category":category}).sort("averageScore2",-1)[0:100]
    #     for document in cursor:
    #         db.top.insert_one(document)
    # Top 100 from all categories
    # cursor = db.top.find().sort("averageScore2", -1)[0:100]
    # for document in cursor:
    #     db.top100.insert_one(document)

    # 100 Popular Apps for each categories
    # categories = db.appStore.distinct("category")
    # for category in categories:
    #     cursor = db.appStore.find({"category": category}).sort("popularScore", -1)[0:100]
    #     for document in cursor:
    #         db.popularApps.insert_one(document)


    # Popular 24 Apps for several categories.
    # cursor = db.appStore.find({"category": "Entertainment"}).sort("popularScore", -1)[0:24]
    # for document in cursor:
    #     db.popularAppsTop24.insert_one(document)
    # cursor = db.appStore.find({"category": "Games"}).sort("popularScore", -1)[0:24]
    # for document in cursor:
    #     db.popularAppsTop24.insert_one(document)
    #
    # cursor = db.appStore.find({"category": "Health & Fitness"}).sort("popularScore", -1)[0:24]
    # for document in cursor:
    #     db.popularAppsTop24.insert_one(document)
    #
    # cursor = db.appStore.find({"category": "News"}).sort("popularScore", -1)[0:24]
    # for document in cursor:
    #     db.popularAppsTop24.insert_one(document)
    # cursor = db.appStore.find({"category": "Productivity"}).sort("popularScore", -1)[0:24]
    # for document in cursor:
    #     db.popularAppsTop24.insert_one(document)
    # cursor = db.appStore.find({"category": "Photo & Video"}).sort("popularScore", -1)[0:24]
    # for document in cursor:
    #     db.popularAppsTop24.insert_one(document)
    # cursor = db.appStore.find({"category": "Music"}).sort("popularScore", -1)[0:24]
    # for document in cursor:
    #     db.popularAppsTop24.insert_one(document)
    # cursor = db.appStore.find({"category": "Shopping"}).sort("popularScore", -1)[0:24]
    # for document in cursor:
    #     db.popularAppsTop24.insert_one(document)
    # cursor = db.appStore.find({"category": "Social Networking"}).sort("popularScore", -1)[0:24]
    # for document in cursor:
    #     db.popularAppsTop24.insert_one(document)
    # cursor = db.appStore.find({"category": "Utilities"}).sort("popularScore", -1)[0:24]
    # for document in cursor:
    #     db.popularAppsTop24.insert_one(document)

    return


if __name__ == '__main__':
    main()
