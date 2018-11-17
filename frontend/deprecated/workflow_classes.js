class Grid{
    constructor(htmlElement){        
        this.nodes = []; 
        this.htmlElement = htmlElement;
        this.idCounter = 0;
        htmlElement.addEventListener('mousedown',(e) => this.mousedown(e));
        htmlElement.addEventListener('mouseup', (e) => this.mouseup(e));
        htmlElement.addEventListener('mousemove', (e) => this.mousemove(e));
        this.selectedNode = null;
        this.idcounter = 0;
    }

    mousedown(e){
        console.log('Mousedown');
        if(e.target == this.htmlElement){
            this.addNode(e.clientX,e.clientY,blankNode);
        }
    }

    mousemove(e) {
        //console.log('Mousemove');
    }

    mouseup(e){
        console.log('Mouseup');
    }

    addNode(x,y,node){
        this.nodes.push(node);

        let tempGroup = document.createElementNS('http://www.w3.org/2000/svg','g');
        tempGroup.id = "node-" + this.idCounter++;

        let tempNode = document.createElementNS('http://www.w3.org/2000/svg','rect');
        tempNode.setAttribute('x',x);
        tempNode.setAttribute('y',y);
        tempNode.setAttribute('width',node.width);
        tempNode.setAttribute('height',node.height);
        tempNode.setAttribute('style',node.style);

        let tempText = document.createElementNS('http://www.w3.org/2000/svg','text');
        tempText.setAttribute('fill', 'black');
        tempText.setAttribute('x',x + 10);
        tempText.setAttribute('y',y + 30);
        tempText.setAttribute('width',node.width - 10);
        tempText.setAttribute('height',node.height - 30);
        tempText.innerHTML = node.name;

        tempGroup.appendChild(tempNode);
        tempGroup.appendChild(tempText);

        this.selectedNode = tempGroup;
        this.htmlElement.appendChild(tempGroup);
    }

    updateNode(){
        
    }
}

class Node{
    constructor(name,width,height,device){
        this.name = name;
        this.width = width;
        this.height = height;
        this.device = device;
        this.style = 'fill:grey;stroke:darkgrey;stroke-width:5';
    }
}

class Device{
    constructor(name,description,inputs,outputs){
        this.name = name;
        this.description = description;
        this.inputs = inputs;
        this.outputs = outputs;
        this.style = 'fill:grey;stroke:darkgrey;stroke-width:5';
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