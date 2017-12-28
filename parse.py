import datetime
import urllib
import json

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
  url = 'https://api.hotslogs.com/Public/Players/'+player['id']
  foo = json.loads(urllib.urlopen(url).read())
  for ranking in foo['LeaderboardRankings']:
      player[ranking['GameMode']] = ranking['CurrentMMR']

f=open("qm_out.txt", "a+")
f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
for name, player in sorted(players.iteritems()):
  print name,player.get('QuickMatch',0)
  f.write(",%s" % player.get('QuickMatch',0))
f.close()

f=open("unranked_out.txt", "a+")
f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
for name, player in sorted(players.iteritems()):
  f.write(",%s" % player.get('UnrankedDraft', 0))
f.close()
