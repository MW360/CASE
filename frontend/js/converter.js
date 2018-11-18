var infile = '<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="2" value="Schalter" vertex="1" connectable="0" parent="1"><mxGeometry x="529" y="122" width="120" height="80" as="geometry"/><Object id="0" name="Schalter" as="data"/></mxCell><mxCell id="3" value="I" vertex="1" parent="2"><mxGeometry x="35" width="10" height="10" as="geometry"/><Object reciever="1" recIn="Inp1" as="data"/></mxCell><mxCell id="4" value="I" vertex="1" parent="2"><mxGeometry x="75" width="10" height="10" as="geometry"/><Object reciever="1" recIn="Inp2" as="data"/></mxCell><mxCell id="5" value="O" vertex="1" parent="2"><mxGeometry x="55" y="70" width="10" height="10" as="geometry"/><Object sender="1" sendOut="Out1" as="data"/></mxCell><mxCell id="6" value="Lampe" vertex="1" connectable="0" parent="1"><mxGeometry x="520" y="360" width="120" height="80" as="geometry"/><Object id="1" name="Lampe" as="data"/></mxCell><mxCell id="7" value="I" vertex="1" parent="6"><mxGeometry x="55" width="10" height="10" as="geometry"/><Object reciever="2" recIn="Inp1" as="data"/></mxCell><mxCell id="8" edge="1" parent="1" source="5" target="7"><mxGeometry relative="1" as="geometry"/></mxCell></root></mxGraphModel>'
var parser = new DOMParser();
var doc = parser.parseFromString(infile, "application/xml");
var cells = doc.getElementsByTagName('mxCell');

var dataCells = [];
var edgeCells = [];
for(cell of cells){
    if(cell.getAttribute('vertex') == 1 && cell.getAttribute('value') !== 'I' && cell.getAttribute('value') !== 'O'){
        let child = cell.children[1];
        dataCells.push({
            'id': child.getAttribute('id'),
            'name': child.getAttribute('name')
        })
    } else if(cell.getAttribute('edge') == 1) {
        let source = cells[cell.getAttribute('source')].children[1];        
        let target = cells[cell.getAttribute('target')].children[1];

        edgeCells.push({
            'sender': source.getAttribute('sender'),
            'reciever': target.getAttribute('reciever'),
            'sendOut': source.getAttribute('sendOut'),
            'recIn': target.getAttribute('recIn')
        })
    }
}

console.log(JSON.stringify(
    {
        'nodes': dataCells,
        'edges': edgeCells
    }
))