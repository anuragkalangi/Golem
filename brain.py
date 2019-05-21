import pymysql.cursors
import tensorflow as tf
import numpy as np 
import json
import random


ProbilityMatrix = np.zeros(shape=(140,140),dtype=object)

def brain() :
	print("thinking...")
	connection = pymysql.connect(host='localhost',
	                             user='golem',
	                             password='whateven',
	                             db='thirst')

	cur = connection.cursor(pymysql.cursors.DictCursor)

	heroId = 44 #phantom assassin
	sql = "SELECT * FROM playerPositions WHERE hero ='%s'"
	cur.execute(sql % heroId)
	result=cur.fetchall()

	for row in result:
		matchVal  = row['matchId']
		time  = row['time']
		x = int(row['x']) - 50
		y = int(row['y']) - 50
		for selectrow in result :
			if selectrow['time']  ==  time + 1:
				if selectrow['matchId'] == matchVal:
					value  = np.array([selectrow['x'],selectrow['y']])
					if ProbilityMatrix[x][y] == 0:
						Data = [value]
						ProbilityMatrix[x][y] = Data
					else:
						array  = ProbilityMatrix[x][y]
						array.append(value)
						ProbilityMatrix[x][y] = array	
	print("done Thinking")


def getNextPosition(origin,commandQueue):
	x = int(((origin[0] + 7000) / 100)) 
	y = int(((origin[1] + 7000) / 100)) 
	value = ProbilityMatrix[x][y]
	if value == 0:
		randx = random.randint(x+48,x+58)
		randy = random.randint(y+48,y+58)
		x = ((randx - 50) * 100) - 7000
		y = ((randy - 50) * 100) - 7000
		value = json.dumps({"x":x,"y":y,"command":"MOVE"})
		print(x)
		print(y)
		commandQueue.append(value)
	else:
		length = len(value)
		index = random.randint(0,length-1)
		pos = value[index]
		x = ((pos[0] - 50) * 100) - 7000
		y = ((pos[1] - 50) * 100) - 7000
		print(x)
		print(y)
		value = json.dumps({"x":x,"y":y,"command":"MOVE"})
		commandQueue.append(value)


	

		
	