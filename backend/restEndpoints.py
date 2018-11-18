import flask
import glob
import json
import os
from flask_cors import CORS, cross_origin
app = flask.Flask('moin')
cors = CORS(app)

# - - - - GET ENDPOINTS - - - -

@app.route('/devices', methods=['GET'])
@cross_origin()
def getDevices():
    templist = []
    jsonFiles = glob.glob('Devices/*.json')
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
    if os.path.isfile('Devices/' + devicename + '.json'):
        with open('Devices/' + devicename + '.json') as json:
            return json.read()
    else:
        return "NOPE", 404
    
@app.route('/workflows', methods=['GET'])
@cross_origin()
def getWorkflows():
    templist = []
    jsonFiles = glob.glob('Workflows/*.json')
    for file in jsonFiles:
        with open(file) as json:
            tempcontent = ''
            for line in json:
                tempcontent = (tempcontent + line.strip())
            templist.append(tempcontent)
    return str(templist).replace('\'','')

@app.route('/workflows/<workflowname>', methods=['GET'])
@cross_origin()
def getWorkflowByName(workflowname):
    if os.path.isfile('Workflows/' + workflowname + '.json'):
        with open('Workflows/' + workflowname + '.json') as json:
            return json.read()
    else:
        return "NOPE", 404


# - - - - POST ENDPOINTS - - - -

@app.route('/devices/<devicename>', methods=['POST'])
@cross_origin()
def postDeviceByName(devicename):
    with open('Devices/' + devicename + '.json','w') as json:
        json.write(flask.request.data.decode('UTF8'))
    return 'Written to disk'

@app.route('/Workflow/<workflowname>', methods=['POST'])
@cross_origin()
def postWorkflowByName(workflowname):
    with open('Workflow/' + workflowname + '.json','w') as json:
        json.write(flask.request.data.decode('UTF8'))
    return 'Written to disk'