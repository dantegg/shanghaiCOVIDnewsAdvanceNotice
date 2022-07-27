from datetime import date
import re
from selenium import webdriver
import datetime
from string import Template
from selenium.webdriver.common.by import By
from win10toast import ToastNotifier
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import time
today = datetime.date.today()
dateString = "${month}月${day}"
dateTemplate = Template(dateString)
todayParam = {"month": today.month, "day": today.day}
todayString = dateTemplate.substitute(todayParam)

# 爬虫爬取live.kankannews.com的信息，查询有无最新的上海发布会
def test():
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    ttdriver = webdriver.Chrome("D:\\tools\\chromedriver\\chromedriver.exe", chrome_options=option)
    vv = ttdriver.get('https://live.kankanews.com/')
    text = ttdriver.page_source
    time.sleep(20)
    items = ttdriver.find_elements(by=By.CLASS_NAME, value="infor")
    for item in items:
        # print(item.text)
        matchStr = re.search(r"上海市第\d+场[\u4e00-\u9fa5]{0,}新闻发布会", item.text)
        if matchStr is not None:
            matchDate = re.search(todayString, item.text)
            if matchDate is not None:
                #print("get fabuhui =====>" + item.text)
                print("success")
                return item.text
        else:
            # print("not found")
            return "not found"

#toast消息提醒有新的发布会
def toastMessage(toastText):
    print("zzz =====" + toastText)
    if toastText == "not found":
        print(toastText)
        toaster = ToastNotifier()
        toaster.show_toast("木有",
        toastText,
        icon_path="test.ico",
        duration=200)
    else:
        print("toast ====" + toastText)
        toaster = ToastNotifier()
        toaster.show_toast("新消息",
            toastText,
            icon_path = "test.ico",
            duration=200)

#定时器，定时执行爬虫,如果今天触发了爬虫，则停止触发并重置
def SpiderTimer():
    print("time")


if __name__ == '__main__':
    toastMessage(test())