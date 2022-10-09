import requests
import urllib
import time
from bs4 import BeautifulSoup
import mysql.connector

r = requests.get('https://www.amnesty.it/entra-in-azione/appelli/')
content = r.content
soup = BeautifulSoup(content)
appelli = []
allLinks = soup.findAll('a', attrs={'class':'box-appeal'})
for index, link in enumerate(allLinks):
    app = {
        'link': '',
        'titolo': '',
        'img': '',
    }
    app['link'] = link['href']
    imgTag = link.find('img')
    title = link.find('div', attrs={'class':'title-container'}).find('h4').text
    app['title'] = title
    if(imgTag is not None):
        app['img'] = imgTag['src']
        img_data = requests.get(imgTag['src']).content
        with open('./downloadedImages/'+str(time.time())+'.jpg', 'wb') as handler:
            handler.write(img_data)

    appelli.append(app)
    prog = format(((index+1)/len(allLinks))*100,'.2f')
    print(str(prog)+'%',end='\r')
    
print(appelli)

