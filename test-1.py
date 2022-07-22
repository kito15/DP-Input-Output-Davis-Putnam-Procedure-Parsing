import DavidPut

clause_list = []
footer = []
atoms = []
afterZ = False
file=input("Enter file name (Example file.txt): ")
input_file = open(file, 'r')
for line in input_file.readlines():
    line = line.replace('\n','')
    if line == "0":
        afterZ = True
    if afterZ:
        footer.append(line)
        continue
    clause = []
    line_elements = line.split()
    for element in line_elements:
        element = int(element)
        clause.append(element)
        atom = abs(element)
        if atom not in atoms:
            atoms.append(atom)
    clause_list.append(clause)
            
print("ATOMS: ", atoms)
print("CLAUSES: ", clause_list)

result = DavidPut.DavisPutnam(atoms, clause_list)
if result == None:
    print("No Solution Found")
else:
    print("Solution Found!")
    for i in result.items():
        if i[1] > 0:
            print(i[0], "true")
        elif i[1] < 0:
            print(i[0], "false")
        else:
            print(i[0], "UNBOUND")    
for item in footer:
    print(item)



