import flask
import glob
import json
import os
from flask_cors import CORS, cross_origin
app = flask.Flask('moin')
cors = CORS(app)

@app.route('/devices', methods=['GET'])
@cross_origin()
def getDevices():
    templist = []
    jsonFiles = glob.glob('devices/*.json')
    for file in jsonFiles:
        with open(file) as json:
            tempcontent = ''
            for line in json:
                tempcontent = (tempcontent + line.strip())
            templist.append(tempcontent)
    return str(templist).replace('\'','')

@app.route('/devices/<devicename>')
@cross_origin()
def getDeviceByName(devicename):
    if os.path.isfile('devices/' + devicename + '.json'):
        with open('devices/' + devicename + '.json') as json:
            return json.read()
    else:
        return "NOPE", 404
    
@app.route('/workflows', methods=['GET'])
@cross_origin()
def getWorkflows():
    templist = []
    jsonFiles = glob.glob('workflows/*.json')
    for file in jsonFiles:
        with open(file) as json:
            tempcontent = ''
            for line in json:
                tempcontent = (tempcontent + line.strip())
            templist.append(tempcontent)
    return str(templist).replace('\'','')

@app.route('/workflows/<workflowname>')
@cross_origin()
def getWorkflowByName(workflowname):
    if os.path.isfile('workflows/' + workflowname + '.json'):
        with open('workflows/' + workflowname + '.json') as json:
            return json.read()
    else:
        return "NOPE", 404