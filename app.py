import requests
import urllib
import time
import json
from bs4 import BeautifulSoup

def handler(event, context):
    r = requests.get('https://www.amnesty.it/entra-in-azione/appelli/')
    content = r.content
    soup = BeautifulSoup(content,features="html.parser")
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
        if(imgTag is not None):
            app['imgUrl'] = imgTag['src']
        sibs = link.next_siblings
        for p in sibs:
            app['short_description'] += p.text
        appelli.append(app)
        prog = format(((index+1)/len(allLinks))*100,'.2f')
    return json.dumps(appelli)
    

