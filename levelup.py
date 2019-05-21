import  json

levelUpOrder = [0,1,0,2,0,3,1,1,4,1,3,2,2,6,3,4,9,10]

def levelupPlayer():
	value = levelUpOrder[0]
	levelUpOrder.remove(value)
	return json.dumps({"abilityIndex":value})