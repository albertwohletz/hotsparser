import requests
from bs4 import BeautifulSoup
import datetime

"""
    Example HTML:
    <tr class="rgRow" id="ctl00_MainContent_RadGridGeneralInformation_ctl00__2">
        <td>Quick Match</td><td><img class="divLeagueImage" src="//d1i1jxrdh2kvwy.cloudfront.net/Images/Leagues/1.png"/>\xa0<span>Diamond 44219 (MMR:\xa02207)</span></td>
    </tr>
"""

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
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
f.write(time+',')
for name, id in ids.iteritems():
  url = 'https://www.hotslogs.com/Player/Profile?PlayerID='+id
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'lxml')
  qm = soup.find('td', text='Quick Match')
  box = qm.findNext('td').find('span').text
  mmr = box[-5:-1]
  f.write(mmr+',')

