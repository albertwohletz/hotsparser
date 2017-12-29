import requests
import re
from bs4 import BeautifulSoup
import datetime

def getMMR(request, search_string):
  soup = BeautifulSoup(request.content, 'lxml')
  td = soup.find('td', text=search_string)
  if td:
      box = td.findNext('td').find('span').text
      return re.findall(r'MMR:.\d+', box)[0].split()[1]
  else:
      return None

def updateFile(key, players):
    f=open(key+'.txt', 'a+')
    f.write('\n')
    f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    for name, player in sorted(players.iteritems()):
      f.write(',%s' % player.get(key,0))
    f.close()

def main():
    players = {
            'Blindo': {'id': '181757'},
            'Tefefe': {'id': '10683361'},
            'Vizoul': {'id': '161824'},
            'Darklink': {'id': '8780497'},
            'QKachoo': {'id': '1066174'},
            'Etiquette': {'id': '171306'},
            'Furasta': {'id': '1492384'},
            'NastyNate': {'id': '292699'},
            'KingBaby': {'id': '6782253'},
            'Mattie': {'id': '161823'},
            'Tilamor': {'id': '1262342'},
    }

    for name, player in players.iteritems():
      url = url = 'https://www.hotslogs.com/Player/Profile?PlayerID='+player['id']
      request = requests.get(url)

      # Get QM
      player['quickmatch'] = getMMR(request, 'Quick Match')
      player['unranked'] = getMMR(request, 'Unranked Draft')
      player['heroleague'] = getMMR(request, 'Hero League')
      player['teamleague'] = getMMR(request, 'Team League')

    # Write Files
    updateFile('quickmatch', players)
    updateFile('unranked', players)
    updateFile('heroleague', players)
    updateFile('teamleague', players)

if __name__ == '__main__':
    main()
