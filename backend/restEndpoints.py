import flask
import glob
import json
from flask_cors import CORS, cross_origin
app = flask.Flask('moin')
cors = CORS(app)

@app.route('/devices', methods=['GET'])
@cross_origin()
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

@app.route('/devices/<devicename>')
@cross_origin()
def api_article(devicename):
    return devicename

@app.route('/workflows', methods=['GET'])
@cross_origin()
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