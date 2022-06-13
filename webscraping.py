
import requests
from bs4 import BeautifulSoup as bs

user_name = "white_strick"
url = "https://github.com/"+user_name
results = requests.get(url)

soup =bs(results.content,"html parser")
profile_pic =soup.find('img',{'alt':'Avvatar'})
print (profile_pic)