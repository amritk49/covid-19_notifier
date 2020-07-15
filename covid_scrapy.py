from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier

header = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/",headers=header)

html = urlopen(req)

soup = bs(html)
new_cases = soup.find("li",{"class":"news_li"}).strong.text.split()[0]

new_death = list(soup.find("li",{"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

notifier = ToastNotifier()
message = "New cases - " + new_cases + "\nDeath - " + new_death

notifier.show_toast(title="COVID-19 UPDATE",msg=message,duration=5,icon_path=r"virus.ico")
