import time
from win10toast import ToastNotifier
import requests

# r = requests.get("https://live.kankanews.com/")
r = requests.get("https://api-app.kankanews.com/kankan/pc/live?nonce=ns4dt2vx&platform=pc&timestamp=1646897946&version=1.0&sign=212c27cf00c56419d95bdf0e044d8251")
# html=r.text.find('class="u2"')
# r.encoding= "utf-8"
contentText = r.json()
# html_doc=str(html,'gb2312') #html_doc=html.decode("utf-8","ignore")
# print(html)
print(contentText['result']['live_notice_list'])
advanceList = contentText['result']['live_notice_list']
for item in advanceList:
    print('title is====' + item['title'])
    print('intro is====' + item['intro'])

# print("==========response" + r.content.decode())

# http://www.shio.gov.cn/sh/xwb/n790/n791/index.html

# toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!",
# "Python is 10 seconds",
# icon_path = "test.ico",
# duration=10)

# while toaster.notification_active():
#     time.sleep(0.1)
# print("hello")