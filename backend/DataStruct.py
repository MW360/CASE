import sys
import json
import os
Workflow = {}
Devices = {}
Scripts = {}
Driver = {}

def GetWorkflows():
    ls = os.listdir("./Workflows/");
    for f in ls:
        if ".json" in f:
            w = open("./Workflows/"+f);
            data = w.read();
            w.close();
            Workflow[f.split(".")[0]] = json.loads(data);

def GetNodes():
    ls = os.listdir("./Devices/");
    for f in ls:
        if ".json" in f:
            w = open("./Devices/" + f);
            data = w.read();
            w.close();
            Devices[f.split(".")[0]] = json.loads(data);
def CreateNewDevice():
    pass

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
            Scripts[f.split(".")[0]] = i;



GetWorkflows();
GetNodes();
GetScript();
print(Workflow.keys());
print(Devices.keys());
print(Scripts.keys());