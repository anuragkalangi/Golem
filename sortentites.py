import json
from heroBuying import buyItems
from brain import getNextPosition

creeps =[]
ourTower = []
enemyTower = []
ourBuilding = []
enemyBuilding = []
ourCreeps= []
enemyCreeps = []

def sortentites(entity,commandQueue):
	jsondata = json.loads(entity)
	for entity in jsondata['entities']:
		data  = jsondata['entities'][entity]
		#print "%s" %data['type']
		if data['type'] == "Hero":
			if data['team'] == 2:
				sortOurBot(data,commandQueue)
			else:
				sortEnemy(data,commandQueue)	
		if data['type'] == "Tower":
			if data['team'] == 2:
				ourTower.append(data)
			else:
				enemyTower.append(data)
		if data['type']	== "Building":
			if data['team'] == 2:
				ourBuilding.append(data)
			else:
				enemyBuilding.append(data)
		if data['type'] == "BaseNPC":
			#print "%s" %data
			if data['team'] == 2:
				ourCreeps.append(data)
			else:
				enemyCreeps.append(data)

			
		
def sortOurBot(hero,commandQueue):
	buyItems(hero['gold'],commandQueue)
	getNextPosition(hero['origin'],commandQueue)


def sortEnemy(hero,commandQueue):
	print "in" 