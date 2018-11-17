import flask
import glob
import json
app = flask.Flask('moin')

@app.route('/devices', methods=['GET'])
def getDevices():
    templist = []
    jsonFiles = glob.glob('./devices/*.json')
    for file in jsonFiles:
        with open(file) as json:
            tempcontent = ''
            for line in json:
                tempcontent = (tempcontent + line.strip())
            templist.append(tempcontent)
    return str(templist).replace('\'','')

@app.route('/workflows', methods=['GET'])
def getWorkflows():
    templist = []
    jsonFiles = glob.glob('workflow/*.json')
    for file in jsonFiles:
        with open(file) as json:
            tempcontent = ''
            for line in json:
                tempcontent = (tempcontent + line.strip())
            templist.append(tempcontent)
    return str(templist).replace('\'','')