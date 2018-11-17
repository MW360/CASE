import time

import DataStruct, copy
running = True;
class Main:
    running = True
    def __init__(self):

        HttpListener();
        ThreadControl();
        self.DeviceStates = {};
        self.DeviceStatesOld = {};
        self.DataStruct = DataStruct.DataStructure();
        self.debug();
        self.main();


    def main(self):
        while Main.running:
            self.GetDeviceStates();
            if self.DeviceStates != self.DeviceStatesOld:
                ChangedInterfaces = []
                for i in self.DeviceStates.keys():
                    if self.DeviceStatesOld[i] != self.DeviceStates[i]:
                        ChangedInterfaces.append(i)

                for workflow_name in self.DataStruct.WorkflowJson.keys():
                    node_names = self.DataStruct.GetNodeNames(workflow_name);
                    print(workflow_name, " ", node_names);
                    print(self.DeviceStates);
                    self.UpdateWorkflow(workflow_name, ChangedInterfaces);
            time.sleep(self.DataStruct.MinUpdateTime / 1000);


    def UpdateWorkflow(self, workflow_name, ChangedDevices):
        if workflow_name not in self.DataStruct.WorkflowJson.keys():
            return
        





    def GetDeviceStates(self):
        self.DeviceStatesOld = copy.deepcopy(self.DeviceStates)
        self.DeviceStates = {};
        for driver_name in self.DataStruct.DriversPy.keys():
            driver = self.DataStruct.DriversPy[driver_name];
            data = driver.Get();
            self.DeviceStates[driver_name] = data;


    def debug(self):
        print(self.DataStruct.WorkflowJson.keys());
        print(self.DataStruct.DevicesJson.keys());
        print(self.DataStruct.ScriptsPy.keys());
        print(self.DataStruct.DriversJson.keys());
        print(self.DataStruct.DriversPy.keys());
        print(self.DataStruct.GetNodeNames("Workflow"));
        print(self.DataStruct.MinUpdateTime);

class HttpListener():
    def __init__(self):
        # START LISTENER HERE
        running = False;
        pass

class ThreadControl():
    def __init__(self):
        # STERT CONTROLLER HERE
        pass




if __name__=="__main__":
   Main();


