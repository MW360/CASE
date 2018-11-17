import DataStruct
running = True;
class Main():
    def __init__(self):
        # DEBUG
        DataStruct.GetWorkflows();
        DataStruct.GetNodes();
        DataStruct.GetScript();
        DataStruct.GetDriver();
        print(DataStruct.WorkflowJson.keys());
        print(DataStruct.DevicesJson.keys());
        print(DataStruct.ScriptsPy.keys());
        print(DataStruct.DriversJson.keys())
        print(DataStruct.DriversPy.keys())
        print(DataStruct.GetNodeNames("Workflow"))
        #DEBUG
        HttpListener();
        ThreadControl();
        self.main();

    def main(self):
        while running:
            pass




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
   Main()

