class Grid{
    constructor(htmlElement){        
        this.nodes = []; 
        this.htmlElement = htmlElement;
        this.idCounter = 0;
        htmlElement.addEventListener('mousedown',(e) => this.mousedown(e));
        htmlElement.addEventListener('mouseup', (e) => this.mouseup(e));
        htmlElement.addEventListener('mousemove', (e) => this.mousemove(e));
        htmlElement.addEventListener('ondrop', (e) => this.drop(e));
    }

    mousedown(e){
        //if(e.target == this.htmlElement){}
    }

    mousemove(e) {

    }

    mouseup(e){

    }

    drop(e){
        let nodeId = e.dataTransfer.getData('id');

    }

    addNode(x,y,node){
        let tempNode = document.createElementNS('http://www.w3.org/2000/svg','rect');
        tempNode.setAttribute('x',x);
        tempNode.setAttribute('y',y);
        tempNode.setAttribute('width',w);
        tempNode.setAttribute('height',h);
        tempNode.setAttribute('style','fill:grey;stroke:darkgrey;stroke-width:5');
        tempNode.id = id;
        this.htmlElement.appendChild(tempNode);
    }
}

class Node{
    constructor(name,x,y,inputs,outputs){
        this.name = name;
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.inputs = inputs;
        this.outputs = outputs;
    }
}

class Input{
    constructor(name,connectedTo){
        this.name = name;
        this.connectedTo = connectedTo;
    }
}

class Output{
    constructor(name){
        this.name = name;
    }
}