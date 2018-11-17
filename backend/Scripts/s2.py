
def Run_Script(inputs, update_outputs):
    in1 = inputs["in1"]
    print(in1)

    out1 = 0
    if in1 > 50:
        out1 = 1
    update_outputs("out1", out1)