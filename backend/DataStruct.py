import sys
import json
import os
WorkflowJson = {}
DevicesJson = {}
ScriptsPy = {}
DriversPy = {}
DriversJson = {}

def GetWorkflows():
    ls = os.listdir("./Workflows/");
    for f in ls:
        if ".json" in f:
            w = open("./Workflows/"+f);
            data = w.read();
            w.close();
            WorkflowJson[f.split(".")[0]] = json.loads(data);

def GetNodes():
    ls = os.listdir("./Devices/");
    for f in ls:
        if ".json" in f:
            w = open("./Devices/" + f);
            data = w.read();
            w.close();
            DevicesJson[f.split(".")[0]] = json.loads(data);
def CreateNewDevice():
    pass
def GetDriver():
    ls = os.listdir("./Driver/");
    for f in ls:
        if "." not in f:
            w = open("./Driver/" + f + "/" + f + ".json");
            data = w.read();
            w.close();
            DriversJson[f.split(".")[0]] = json.loads(data);

            filepath = "Driver/" + f + "/" +f
            directory, fnc_name = os.path.split(filepath)
            path = list(sys.path)
            sys.path.insert(0, directory)

            try:
                i = __import__(f.split(".")[0])
            finally:
                sys.path[:] = path
            DriversPy[f.split(".")[0]] = i;


def GetScript():
    ls = os.listdir("./Devices/");
    for f in ls:
        if ".py" in f:
            filepath = "Devices/" + f

            directory, fnc_name = os.path.split(filepath)

            path = list(sys.path)
            sys.path.insert(0, directory)

            try:
                i = __import__(f.split(".")[0])
            finally:
                sys.path[:] = path
            ScriptsPy[f.split(".")[0]] = i;

def GetNodeNames(workflowname):
    if workflowname not in WorkflowJson.keys():
        return
    print(WorkflowJson[workflowname]);
    l = []
    for node in WorkflowJson[workflowname]["nodes"]:
        l.append(node["name"])
    return l


