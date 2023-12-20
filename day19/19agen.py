import regex as re
ofile = open("workflows.py", "w")
for line in open("workflows","r"):
    line = line.strip()
    m = re.match("(.*?)\{(.*?)\}", line)
    wfname = m[1]
    wfrules = m[2]
    print(wfname, wfrules)
    ofile.write(f"def f_{wfname}(x,m,a,s):\n")
    wfrules = wfrules.strip()
    for rule in wfrules.split(','):
        if ':' in rule:
            r, n = rule.split(':')
            r = r.strip()
            n = n.strip()
            ofile.write(f"    if {r}:\n")
            if n == 'A':
                ofile.write("        return True\n")
            elif n == 'R':
                ofile.write("        return False\n")
            else:
                ofile.write(f"        return f_{n}(x,m,a,s)\n")
        else:
            rule = rule.strip()
            if rule == 'A':
                ofile.write("    return True\n")
            elif rule == 'R':
                ofile.write("    return False\n")
            else:
                ofile.write(f"    return f_{rule}(x,m,a,s)\n")
ofile.close()

ofile = open("parts.py", "w")
ofile.write("from workflows import *\n")
ofile.write("res = 0\n")
for line in open("parts"):
    line = line.strip()
    for v in ['x','m','a','s']:
        line = line.replace(f'{v}',f'"{v}"')
    line = line.replace('=',':')
    ofile.write(f"i = {line}\n")
    ofile.write(f"if f_in(**i):\n")
    ofile.write(f"    res += sum(i.values())\n")
ofile.write("print(res)")

