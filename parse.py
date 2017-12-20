import requests
import re
from bs4 import BeautifulSoup
import datetime

ids = {
        'Blindo': '181757',
        'Tefefe': '10683361',
        'Vizoul': '161824',
        'Darklink': '8780497',
        'QKachoo': '1066174',
        'Etiquette': '171306',
        'Furasta': '1492384',
        'NastyNate': '292699',
        'KingBaby': '6782253',
        'Mattie': '161823'
}

f=open("out.txt", "a+")
f.write('\n')
f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

for name, id in ids.iteritems():
  url = 'https://www.hotslogs.com/Player/Profile?PlayerID='+id
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'lxml')
  qm = soup.find('td', text='Quick Match')
  box = qm.findNext('td').find('span').text
  mmr = re.findall(r'MMR:.\d+', box)[0].split()[1]
  f.write(",%s" % mmr)

f.close()
