
def Run_Script(inputs, update_outputs):
    sum = inputs['Inp1'] + inputs['Inp2']
    update_outputs("Out1", sum+1)
