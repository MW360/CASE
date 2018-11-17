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
        self.connections[(src_id, src_socket)] = (dest_id, dest_socket)

    def new_id(self):
        self.id_counter+=1
        if self.id_counter in self.nodes:
            return self.new_id()
        return self.id_counter

    def update_value(self, src_id, src_socket, new_val):
        for c in self.connections:
            if c[0] == src_id and c[1] == src_socket:
                d = self.connections[c]
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
        print("update out: {} {}<-{}".format(output_id, self.outputs[output_id], new_val))
        if self.outputs[output_id] != new_val:
            print("yes update")
            self.outputs[output_id] = new_val
            self.graph.update_value(self.graph_id, output_id, new_val)
        else:
            print("no update")

    def update_in(self, input_id, new_val):
        print("update in: {} {}<-{}".format(input_id, self.inputs[input_id], new_val))
        self.inputs[input_id] = new_val
        self.execute()

    def execute(self):
        self.script.Run_Script(self.inputs, self.update_out)






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
