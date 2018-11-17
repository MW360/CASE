import sys
import json
import os
class DataStructure:


    def __init__(self):
        self.WorkflowJson = {};
        self.DevicesJson = {};
        self.ScriptsPy = {};
        self.DriversPy = {};
        self.DriversJson = {};
        self.MinUpdateTime = 5000;

        self.GetWorkflows();
        self.GetNodes();
        self.GetScript();
        self.GetDriver();
        self.GetMinUpdateTime();


    def GetWorkflows(self):
        ls = os.listdir("./Workflows/");
        for f in ls:
            if ".json" in f:
                w = open("./Workflows/"+f);
                data = w.read();
                w.close();
                self.WorkflowJson[f.split(".")[0]] = json.loads(data);

    def GetNodes(self):
        ls = os.listdir("./Interfaces/");
        for f in ls:
            if ".json" in f:
                w = open("./Interfaces/" + f);
                data = w.read();
                w.close();
                self.DevicesJson[f.split(".")[0]] = json.loads(data);

    def CreateNewDevice(self):
        pass



    def GetDriver(self):
        ls = os.listdir("./Interfaces/");
        for f in ls:
            if "." not in f:
                w = open("./Interfaces/" + f + "/" + f + ".json");
                data = w.read();
                w.close();
                self.DriversJson[f.split(".")[0]] = json.loads(data);

                filepath = "Interfaces/" + f + "/" +f
                directory, fnc_name = os.path.split(filepath)
                path = list(sys.path)
                sys.path.insert(0, directory)

                try:
                    i = __import__(f.split(".")[0])
                finally:
                    sys.path[:] = path
                    self.DriversPy[f.split(".")[0]] = i.Driver();


    def GetScript(self):
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
                    self.ScriptsPy[f.split(".")[0]] = i;

    def GetNodeNames(self, workflowname):
        if workflowname not in self.WorkflowJson.keys():
            return
        l = []
        for node in self.WorkflowJson[workflowname]["nodes"]:
            l.append(node["name"])
        return l

    def TestNodeType(self, device_name):
        if device_name in self.DevicesJson.keys():
            return "Device"
        elif device_name in self.ScriptsPy.keys():
            return  "Script"
        else:
            return ""

    def GetMinUpdateTime(self):
        for driver_name in self.DriversJson.keys():
            try:
                if self.DriversJson[driver_name]["updateTime"] < self.MinUpdateTime:
                    self.MinUpdateTime = self.DriversJson[driver_name]["updateTime"];
            except KeyError:
                pass


