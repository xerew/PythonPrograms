file1 = raw_input("Insert file with python code here: ") #O xristis topothetei to path tou arxheiou me kodika python
with open(file1, 'r') as f:
    lines = f.readlines()
file2 = raw_input("Insert the name of the file containing the python code without the comments: ") #o xristis onomazei to neo arxeio xwris sxolia
with open(file2, 'w') as f:
    for line in lines:
        # Afinoume to #! gia ta Shebang Lines
        if line[0:2] == "#!":
            f.writelines(line)
        # Afinoume tis kenes grammes
        elif not line.strip():
            f.writelines(line)
        # Afairoume ta sxolia apo tis alles grammes
        else:
            line = line.split('#')
            stripped_string = line[0].rstrip()
            # Grafoume tin grammi an to sxolio itan meta ton kodika
            # Afairoume tis grammes pou exoun mono sxolia
            if stripped_string:
                f.writelines(stripped_string)
                f.writelines('\n')
print "Success. Comments are removed!"