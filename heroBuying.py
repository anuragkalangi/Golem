import json

#problems in lightbringer - does not buy items if out of the range of a shop

buyorder = ["item_faerie_fire","item_branches","item_blight_stone","item_poor_mans_shield","item_phase_boots","item_desolator"]

with open('items.json') as data_file:    
    data = json.load(data_file)
    items = data['result']['items']


def  buyItems(gold,commandQueue):
	itemToBuy = buyorder[0];
	for item in items:
		if item['name'] == itemToBuy:
			if gold >= item['cost']:
				value = json.dumps({ "command" : "BUY" , "item" : itemToBuy})
				buyorder.remove(itemToBuy)
				commandQueue.append(value)
				print "%s" %value
				print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
 