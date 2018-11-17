


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

    def update_value(self, src_id, src_socket):
        print(self.connections[(1, 'move')])
        print(self.connections[(src_id, src_socket)])
        tuple1 = (1, 'move')
        print(self.connections.get(tuple1))
        print(self.connections.get((1, 'move')))
        print(self.connections.get((src_id, src_socket)))


class Node(object):
    def __init__(self, script, inputs = {}, outputs = {}, graph = None, graph_id = 0):
        self.script = script
        self.inputs = inputs
        self.outputs = outputs
        self.graph = graph
        self.graph_id = graph_id

    # only update the dependent nodes if our value has changed
    def update_out(self, output_id, new_val):
        if self.outputs[output_id] != new_val:
            self.outputs[output_id] = new_val
            graph.update_value(self.graph_id, output_id)

    def update_in(self, input_id, new_val):
        self.inputs[input_id] = new_val
        execute()

    def execute(self):
        script.run()




# "tests"
x1 = UpdateGraph({}, {})
x1.add_node(Node('a'))
x1.add_node(Node('c'))
x1.add_connection(1, 'move', 2, 'light on')
x1.add_connection(1, 'move', 3, 'light off')
for i in x1.nodes:
    print(x1.nodes[i].script)
print(x1.connections)

