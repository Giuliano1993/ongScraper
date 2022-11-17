import requests
import urllib
import time
import json
from bs4 import BeautifulSoup

#import mysql.connector
#from mysql.connector import errorcode
#try:
#    mydb = mysql.connector.connect(
#        host="mysqldb",
#        user="root",
#        password="secret",
#        port="4306",
#        database="ongScraper"
#    )
#except mysql.connector.Error as err:
#    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#        print("Something is wrong with your user name or password")
#    elif err.errno == errorcode.ER_BAD_DB_ERROR:
#        print("Database does not exist")
#    else:
#        print(err)
#else:
#    mydb.close()

r = requests.get('https://www.amnesty.it/entra-in-azione/appelli/')
content = r.content
soup = BeautifulSoup(content)
appelli = []
allLinks = soup.findAll('a', attrs={'class':'box-appeal'})
for index, link in enumerate(allLinks):
    app = {
        'link': '',
        'titolo': '',
        'imgUrl': '',
        'image_file_name': '',
        'short_description':''
    }
    app['link'] = link['href']
    imgTag = link.find('img')
    title = link.find('div', attrs={'class':'title-container'}).find('h4').text
    app['titolo'] = title
    sibs = link.next_siblings
    for p in sibs:
        app['short_description'] += p.text
    if(imgTag is not None):
        app['imgUrl'] = imgTag['src']
        img_data = requests.get(imgTag['src']).content
        filename = str(time.time())+'.jpg'
        with open('./downloadedImages/'+filename, 'wb') as handler:
            handler.write(img_data)
        app['image_file_name'] = filename
    appelli.append(app)
    prog = format(((index+1)/len(allLinks))*100,'.2f')
    print(str(prog)+'%',end='\r')
    
print(appelli)

