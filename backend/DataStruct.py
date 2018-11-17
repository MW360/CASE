import DataClass
import json
Workflow = {}


def GetWorkflow(workflow):
    data = json.loads(workflow);



def GenerateNodes():
    node = DataClass.Node();
    node.name = "Hallo";
    node.description = "...";
    node.inputs = []

    inp = DataClass.Input();
    inp.name = "Input0";
    inp.type = "bool";
    inp.description = "...";
    node.inputs.Append(inp);

    inp = DataClass.Input();
    inp.name = "Input1";
    inp.type = "bool";
    inp.description = "...";
    node.inputs.Append(inp);

    out = DataClass.Output();

    





    pass;


w = open("./venv/Workflow.json", "r");
r = w.read();
GetWorkflow(r);