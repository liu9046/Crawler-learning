import urllib.request as req
import bs4
import requests

token = 'z0DTPTNKSwt65bSwUd9XrDKeEQtfk5gUciJg0x4k3Lj'
url = "https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data,"html.parser")
titles = root.find("p", class_="JQdotdotdot")

result = titles.string
print(result)

token = 'z0DTPTNKSwt65bSwUd9XrDKeEQtfk5gUciJg0x4k3Lj'
if result != result:
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    params = {"message":"網站有新的消息"}


    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
    print(r.status_code)
