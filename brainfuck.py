import os.path

def load_btf(path: str):
    head = False
    body = False
    flags = dict()
    trans = dict()
    max_chars = 0
    f = open(path,"r")
    line = f.readline()

    while line:
        line = line.strip()
        if line == "'HEAD":
            head = True
            line = f.readline()
            continue
        if line == "'BODY":
            line = f.readline()
            head = True
            break
        if head:
            values = line.split(None,1)
            flags[values[0]] = True if len(values) == 1 else values[1]
        line = f.readline()

    if not body:
        f.close()
        raise IOError("No Body found in btf file")

    while line:
        line = line.strip()
        values = line.split(None,1)
        if len(values[0])>max_chars:
            max_chars=len(values[0])
        trans[values[0]]=values[1]
        line = f.readline()
    
    f.close()
    return flags, trans, max_chars

path = input("Insert name of Coding [default: brainfuck]\n")
found = os.path.isfile(path)
if not found:
    found = os.path.isfile("btf/" + path)
    if found:
        path = "btf/" + path
    else:
        found = os.path.isfile("btf/" + path + ".btf")
        if found:
            path = "btf/" + path + ".btf"
        else:
            path = "btf/brainfuck.btf"

flags, trans, max_chars = load_btf(path)

print (flags)
print (trans)
print (max_chars)

path = input("Insert name of C++Template [default: fixed-size]")
found = os.path.isfile(path)
if not found:
    found = os.path.isfile("template/" + path)
    if found:
        path = "template/" + path
    else:
        found = os.path.isfile("template/" + path + ".cpp")
        if found:
            path = "template/" + path + ".cpp"
        else:
            path = "template/fixed-size.cpp"
print(path)

