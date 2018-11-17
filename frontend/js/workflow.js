var workflowGrid = new Grid(document.getElementById("workflow-grid"));
var nodelist = [];

var graph = new mxGraph(document.getElementById("workflow-grid"));
graph.setConnectable(true)
graph.setPortsEnabled(false)

new mxRubberband(graph)

var parent = graph.getDefaultParent()


var h = document.getElementById('h')
var fn = () => {
    graph.getModel().beginUpdate()
    //Could be put into function that is called for each node
    try {
        let square = graph.insertVertex(parent, null, "X", 10, 10, 100, 50, 'rounded')
        square.setConnectable(false)
        graph.insertVertex(square, null, "Y", 0, 0, 10, 10)
    } finally {
        graph.getModel().endUpdate()
    }
}



mxUtils.makeDraggable(h, graph, fn, null, 0, 0, true, true)