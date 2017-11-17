import os.path


def check_btf_path(path: str) -> str:
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
    return path


def check_cpp_path(path: str) -> str:
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
    return path


def load_btf(path: str) -> tuple:
    head = False
    body = False
    flags = dict()
    trans = dict()
    max_chars = 0
    f = open(path, "r")
    line = f.readline()

    while line:
        line = line.strip()
        if line == "'HEAD":
            head = True
            line = f.readline()
            continue
        if line == "'BODY":
            line = f.readline()
            body = True
            break
        if head:
            values = line.split(None, 1)
            flags[values[0]] = True if len(values) == 1 else values[1]
        line = f.readline()

    if not body:
        f.close()
        raise IOError("No Body found in btf file")

    while line:
        line = line.strip()
        values = line.split(None, 1)
        if len(values[0]) > max_chars:
            max_chars = len(values[0])
        trans[values[0]] = values[1]
        line = f.readline()

    f.close()
    return flags, trans, max_chars


def to_assembler(src: str, trans: dict, max_chars: int) -> str:
    res = ""
    i = 0
    j = 0
    tmp = ""
    while i < len(src):
        tmp += src[i + j]
        if tmp in trans:
            res += trans[tmp] + " "
            i += 1 + j
            j = 0
            tmp = ""
        else:
            j += 1
        if j == max_chars or i + j >= len(src):
            j = 0
            tmp = ""
            i += 1
    return res


def to_flag_string(flags: dict) -> str:
    res = ""
    for key, val in flags.items():
        if val == True:
            res += "#define %s\n" % key
        else:
            res += "#define %s %s\n" % (key, val)
    return res


def create_cpp_src(path: str, assembler: str, flags: dict) -> str:
    res = ""
    f = open(path, "r")
    line = f.readline()
    while line:
        line = line.strip()
        if line.startswith("#brainfuck code"):
            res += "%s\n" % assembler
        elif line.startswith("#brainfuck flags"):
            res += "%s\n" % flags
        else:
            res += "%s\n" % line
        line = f.readline()
    return res


def compile(code: str) -> None:
    file = open('tmp.cpp', 'w')
    file.write(code)
    file.close()
    os.system("g++ -std=c++11 tmp.cpp")
    os.system("rm tmp.cpp")


flags, trans, max_chars = load_btf(check_btf_path(input("Insert name of Coding [default: brainfuck]\n")))
compile(create_cpp_src(check_cpp_path(input("Insert name of C++Template [default: fixed-size]\n")),
                       to_assembler(input("Please insert your Code\n"), trans, max_chars), to_flag_string(flags)))
