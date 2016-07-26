#Product Requirement Document #
## 1.data ##

### app information: ###
+ title
+ id
+ link
+ description
+ launch time
+ average rating(current version/all versions)
+ rating count(current version/all versions)
+ screen shot(img)
+ logo(img)
+ category
+ alphabet


### recommendation ###
+ recommendation list

## 2.homepage ##
+ logo, app collections, search
+ popular apps
+ Browse by category
+ you may like

## 3.app page ##
+ logo
+ title(category,launch time,rating,rating count)
+ description
+ screen shots
+ recommendation

## 4.Question ##
+ download implementation:应用内直接跳转到App Store
+ 中文title如何按首字母排序
+ crawler throws a message:[scrapy] DEBUG: Ignoring response <403 https://itunes.apple.com/us/app/remote/id284417350?mt=8>: HTTP status code is not handled or not allowed: 1)Adding 403 to RETRY_HTTP_CODES in the settings.py  2)The RETRY_TIMES handles how many times to try an error page, by default it is set to 2, and you can override it on the settings.py file. reference:http://stackoverflow.com/questions/34128490/how-to-reschedule-403-http-status-codes-to-be-crawled-later-in-scrapy

