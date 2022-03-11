# from nis import match
import time
from win10toast import ToastNotifier
import requests
import datetime
import re
import time

recordCheck = True
recordDate = datetime.date.today()
todayReportCheck = False

def getNotice(nowDate):
    global recordDate
    global todayReportCheck
    if nowDate == recordDate:
        print("====today check")
        if todayReportCheck is False:
            print("===reporting===")
            result = True
            r = requests.get("https://api-app.kankanews.com/kankan/pc/live?nonce=ns4dt2vx&platform=pc&timestamp=1646897946&version=1.0&sign=212c27cf00c56419d95bdf0e044d8251")
            contentText = r.json()
            advanceList = contentText['result']['live_notice_list']
            # advanceList = [{
            #     "title": '123',
            #     "intro": '邬惊雷'
            # }]
            todayMonth = datetime.date.today().month
            todayDay = datetime.date.today().day
            for item in advanceList:
            # print('title is====' + item['title'])
            # print('intro is====' + item['intro'])
                title = item['title']
                intro = item['intro']
                matchStr = re.search('邬惊雷', intro)
            # result = matchStr.search(intro)
            # print( matchStr)
                if matchStr is not None:
                # print(title)
                # print(intro)
                # print(matchStr.group())
                    toaster = ToastNotifier()
                    toaster.show_toast(title,
                    intro,
                    icon_path = "test.ico",
                    duration=20)
                    print("advance notice get!")
                    result = False
                    todayReportCheck = True
                    print("RECORD_CHECK!!!")
                    print('TODAY_END!!!')
                else:
                    result = True
            if result == True:
                print("NOT_FOND")
            return result
        else:
            return True
    else:
        recordDate = datetime.date.today()
        todayReportCheck = False
        print("=== new Day reset ===")
        return True

    

def sleepTime(hour, minute, second):
    return hour * 3600 + minute * 60 + second

tenMinutes = sleepTime(0,5,0)

while recordCheck:
    time.sleep(tenMinutes)
    nowTime = datetime.date.today()
    if getNotice(nowTime) is False:
        print('QUERY HAPPEN!!!')
        continue
print("end")


