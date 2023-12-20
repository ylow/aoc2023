import regex as re

def gen_constraint(rule):
    if rule[1] == '>':
        return f"Range(start={rule[2:]}, include_start=False)"
    elif rule[1] == '<':
        return f"Range(end={rule[2:]}, include_end=False)"
    else:
        assert(False)

ofile = open("workflowsb.py", 'w')
ofile.write("from ranges import *\n")
ofile.write("from dictrange import *\n")
for line in open("workflows","r"):
    line = line.strip()
    m = re.match("(.*?)\{(.*?)\}", line)
    wfname = m[1]
    wfrules = m[2]
    print(wfname, wfrules)
    ofile.write(f"def f_{wfname}(inrange):\n")
    ofile.write(f"    print('{wfname}',inrange)\n")
    ofile.write("    subrange = inrange.copy()\n")
    ofile.write("    acceptcount = 0\n")
    wfrules = wfrules.strip()
    for rule in wfrules.split(','):
        if ':' in rule:
            r, n = rule.split(':')
            r = r.strip()
            n = n.strip()
            g = gen_constraint(r)
            ofile.write(f"    constraint = {g}\n")
            ofile.write(f"    localrange = subrange.copy()\n")
            ofile.write(f"    localrange['{r[0]}'] = localrange['{r[0]}'].intersection(constraint)\n")
            if n == 'A':
                ofile.write("    acceptcount += localrange.length()\n")
            elif n == 'R':
                ofile.write("\n")
            else:
                ofile.write(f"    acceptcount += f_{n}(localrange)\n")
            ofile.write(f"    subrange['{r[0]}'] = subrange['{r[0]}'].intersection(constraint.complement())\n")
        else:
            rule = rule.strip()
            if rule == 'A':
                ofile.write(f"    acceptcount += subrange.length()\n")
                ofile.write(f"    return acceptcount\n")
            elif rule == 'R':
                ofile.write(f"    return acceptcount\n")
            else:
                ofile.write(f"    acceptcount += f_{rule}(subrange)\n")
                ofile.write(f"    return acceptcount\n")
ofile.write("initial = DictRange()\n")
ofile.write("initial.init_default()\n")
ofile.write("r = f_in(initial)\n")
ofile.write("print(r)\n")
ofile.close()

