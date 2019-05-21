from flask import Flask, redirect, url_for, request, json
from levelup  import levelupPlayer
import sortentites
from brain import brain

#check = True

brain()
commandQueue = []

app = Flask(__name__)

@app.route('/Dota2AIService')
def hello():
	return "Dota2 AI Servicer."

@app.route('/Dota2AIService/reset', methods = ['POST'] )
def reset():
	print "reset method"
	return ""

@app.route('/Dota2AIService/select', methods = ['POST'])
def select():
	print "selecting hero"
	return json.dumps({"hero":"npc_dota_hero_phantom_assassin","command":"SELECT"})

@app.route('/Dota2AIService/chat', methods = ['POST'])
def chat():
	print "chat text %s" %request.form['text']
	return ""

@app.route('/Dota2AIService/levelup', methods = ['POST'])
def levelup():
	value = levelupPlayer()
	print "%s" %value 
	return value

@app.route('/Dota2AIService/update', methods = ['POST'])
def update():
	#print "%s" %commandQueue
	returnVal = ""
	sortentites.sortentites(request.data,commandQueue)
	if len(commandQueue) > 0:
		returnVal = commandQueue[0]  
		commandQueue.remove(returnVal)
	else:
		returnVal = json.dumps({ "command" : "NOOP" })	
	return returnVal



if __name__ == '__main__':
   app.run(host='0.0.0.0')