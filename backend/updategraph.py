import json
import sys
import os

class Sript_Reader(object):
    def __init__(self):
        self.ScriptsPy = {}

    def GetScript(self):
        ls = os.listdir("./Scripts/")
        for f in ls:
            if ".py" in f:
                filepath = "Scripts/" + f

                directory, fnc_name = os.path.split(filepath)

                path = list(sys.path)
                sys.path.insert(0, directory)

                try:
                    i = __import__(f.split(".")[0])
                finally:
                    sys.path[:] = path
                    self.ScriptsPy[f.split(".")[0]] = i


class UpdateGraph(object):
    def __init__(self, nodes = {}, connections = {}):
        self.nodes = nodes
        self.connections = connections
        self.id_counter = 0

    def add_node(self, node):
        new_id = self.new_id()
        self.nodes[new_id] = Node(node.script, node.inputs, node.outputs, self, new_id)

    def add_connection(self, src_id, src_socket, dest_id, dest_socket):
        if (src_id, src_socket) not in self.connections:
            self.connections[(src_id, src_socket)] = []
        self.connections[(src_id, src_socket)].append((dest_id, dest_socket))

    def new_id(self):
        self.id_counter+=1
        if self.id_counter in self.nodes:
            return self.new_id()
        return self.id_counter

    def update_value(self, src_id, src_socket, new_val):
        c = (src_id, src_socket)
        if c in self.connections:
            for d in self.connections[c]:
                print("connection: {} -> {}".format(c, d))
                dest_id = d[0]
                dest_socket = d[1]
                self.nodes[dest_id].update_in(dest_socket, new_val)


class Node(object):
    def __init__(self, script, inputs = {}, outputs = {}, graph = None, graph_id = 0):
        self.script = script
        self.inputs = inputs
        self.outputs = outputs
        self.graph = graph
        self.graph_id = graph_id

    # only update the dependent nodes if our value has changed
    def update_out(self, output_id, new_val):
        print("update out: {} {}<={}".format(output_id, self.outputs[output_id], new_val))
        if self.outputs[output_id] != new_val:
            print("yes update")
            self.outputs[output_id] = new_val
            self.graph.update_value(self.graph_id, output_id, new_val)
        else:
            print("no update")

    def update_in(self, input_id, new_val):
        print("update in: {} {}<={}".format(input_id, self.inputs[input_id], new_val))
        self.inputs[input_id] = new_val
        self.execute()

    def execute(self):
        self.script.Run_Script(self.inputs, self.update_out)





"""
# "tests"
x1 = UpdateGraph()
x2 = Sript_Reader()
x2.GetScript()
x1.add_node(Node(x2.ScriptsPy['s1'], {}, {"out1": 0}))
x1.add_node(Node(x2.ScriptsPy['s2'], {"in1": 7}, {"out1": 0}))

x1.add_connection(1, 'out1', 2, 'in1')
print(x1.connections)


for i in x1.nodes:
    print(x1.nodes[i].script)
for c in x1.connections:
    print(c)
"""

j1 = json.loads("""
{
    "nodes": [
        {
            "id": "1",
            "name":"Add",
            "x":123,
            "y":123
        },
        {
            "id": "2",
            "name":"Add",
            "x":123,
            "y":123
        }
    ],
    "connections": [
        {
            "sender": "1",
            "reciever": "2",
            "sendOut": "Out1",
            "recIn": "Inp1"
        },
        {
            "sender": "1",
            "reciever": "2",
            "sendOut": "Out1",
            "recIn": "Inp2"
        }
    ]
}
""" )


print(j1)

print(j1['nodes'])
print(j1['connections'])

def get_script(name):
    ls = os.listdir("./Scripts/")
    if "{}.py".format(name) in ls:
        print("{}.py".format(name))
        filepath = "Scripts/" + name + ".py"
        directory, fnc_name = os.path.split(filepath)

        path = list(sys.path)
        sys.path.insert(0, directory)
        try:
            i = __import__(name)
        finally:
            sys.path[:] = path
            return i


def get_spec(name):
    ls = os.listdir("./Devices/");
    for f in ls:
        if "{}.json".format(name) in f:
            print("{}.json".format(name))
            path = "Devices/" + f
            with open(path) as f:
                read_data = f.read()

            return json.loads(read_data)


def parse_from_json(json_file):
    workflow = UpdateGraph()
    nodes = {}
    for n in json_file['nodes']:
        print("n:{}".format(n))
        node_id = n['id']
        script = get_script(n['name'])
        spec = get_spec(n['name'])
        print(spec)
        inputs = {}
        for i in spec['inputs']:
            inputs[i['name']] = 0
        outputs = {}
        for i in spec['outputs']:
            outputs[i['name']] = 0
        n_new = Node(script, inputs, outputs, workflow, node_id)
        print(n_new)
        nodes[node_id] = n_new
    for c in json_file['connections']:
        workflow.add_connection(c['sender'], c['sendOut'], c['reciever'], c['recIn'])
    workflow.nodes = nodes
    return workflow


x5 = parse_from_json(j1)

for i in x5.nodes:
    n = x5.nodes[i]
    print("node {} {}, i:{}, o:{}".format(n.graph_id, n.script, n.inputs, n.outputs))
for c in x5.connections:
    print("{} -> {}".format(c, x5.connections[c]))
x5.nodes["1"].execute()