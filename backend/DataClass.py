
class Workflow():
    def __init__(self):
        self.nodes = {};
        self.connections = {}

class Node():

    def __init__(self):
        self.id;
        self.name;
        self.x;
        self.y;

class Connection:
    def __init__(self):
        self.sender;
        self.reciever;
        self.sendOut;
        self.recIn;


class Input():
    def __init__(self):
        self.name;
        self.type;
        self.description;

class Output():
    def __init__(self):
        self.name;
        self.type;
        self.description;


class Device():
    def __init__(self):
        self.name;
        self.description;
        self.inputs = [];
        self.outputs = [];
