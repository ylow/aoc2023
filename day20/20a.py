
HIGH = True 
LOW = False

class FF(object):
    def __init__(self):
        self.state = False

    def connect_input(self, sender):
        pass

    def signal(self, sender, sig):
        if sig == LOW:
            if self.state == False:
                self.state = True
                return HIGH
            elif self.state == True:
                self.state = False
                return LOW
        return None

class Conj(object):
    def __init__(self):
        self.state = {}

    def connect_input(self, sender):
        self.state[sender] = LOW

    def signal(self, sender, sig):
        assert(sender in self.state)
        self.state[sender] = sig
        if all([v == HIGH for v in self.state.values()]):
            return LOW
        else:
            return HIGH

class Broadcast(object):
    def __init__(self):
        pass

    def connect_input(self, sender):
        pass

    def signal(self, sender, sig):
        return sig


class Empty(object):
    def __init__(self):
        pass

    def connect_input(self, sender):
        pass

    def signal(self, sender, sig):
        pass

mods = {}
lines = [x.strip() for x in open('input','r')]
out_edges = {}
for l in lines:
    modname, outputs = [x.strip() for x in l.split("->")]
    newmod = None
    if modname == 'broadcaster':
        newmod = Broadcast()
    elif modname[0] == '%':
        newmod = FF()
        modname = modname[1:]
    elif modname[0] == '&':
        newmod = Conj()
        modname = modname[1:]
    assert(newmod is not None)
    mods[modname] = newmod

    outputs = [x.strip() for x in outputs.split(',')]
    out_edges[modname] = outputs

for mod,v in out_edges.items():
    for outmod in v:
        if outmod not in mods:
            mods[outmod] = Empty()
        mods[outmod].connect_input(mod)

print(mods)
print(out_edges)

from collections import deque
signals_queue = deque()
signals_ctr = {LOW:0, HIGH:0}
def process_signal(sender, signal, receiver, mods, out_edges, out_queue):
    res = mods[receiver].signal(sender, signal)
    if res is not None:
        #print("---", sender, signal, receiver, res)
        signals_ctr[res] += len(out_edges[receiver])
        for e in out_edges[receiver]:
            out_queue.append((receiver, res, e))

for button in range(1000):
    signals_queue.append(("button", LOW, "broadcaster"))
    signals_ctr[LOW] += 1
    while True:
        try:
            sender, signal, receiver = signals_queue.popleft()
        except IndexError:
            break
        process_signal(sender, signal, receiver, mods, out_edges, signals_queue)

print(signals_ctr)
print(signals_ctr[LOW] * signals_ctr[HIGH])
