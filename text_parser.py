import ast_generator

from itertools import cycle


def pygccxml_text_parser(filename):
    """
    Parsing the abstract representation generated by pygccxml
    : class_name a bit hardcoded so namespace specified explicitly
    """
    ast_generator.pygccxml_parser(filename)
    # Need to implement a function to store the output in form of txt file
    with open('pygccxml_ast.txt', 'r') as file_object:
        lines = file_object.readlines()

    namespace_name = []
    namespace_index = []
    for line in lines:
        if 'namespace_t' in line:
            namespace_name.append(line.split(": ")[1].strip().replace("'", ""))
            namespace_index.append(lines.index(line))

    if namespace_name[0] == 'sample_namespace':
        lines = lines[0:]
    else:
        raise Exception('Wrongly specified namespace!')

    class_name = []
    class_index = []
    for line in lines:
        if 'class_t' in line:
            class_name.append(line.split(": ")[1].strip().replace("'", ""))
            class_index.append(lines.index(line))
    class_index.append(len(lines))

    classes = []
    running = True
    licycle = cycle(class_index)
    nextelem = next(licycle)
    while running:
        thiselem, nextelem = nextelem, next(licycle)
        classes.append(lines[thiselem:nextelem])
        if nextelem == class_index[0]:
            running = False
    classes.pop()

    constructor_index = []
    public_constructor = []
    protected_constructor = []
    private_constructor = []
    for line in lines:
        if 'public' in line:
            constructor_index.append(lines.index(line))
            print(line)
        if 'protected' in line:
            constructor_index.append(lines.index(line))
        if 'private' in line:
            constructor_index.append(lines.index(line))

    public_constructor = lines[constructor_index[0]: constructor_index[1]]
    protected_constructor = lines[constructor_index[1]: constructor_index[2]]
    private_constructor = lines[constructor_index[2]: ]

