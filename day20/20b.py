
HIGH = True 
LOW = False
DONE = False

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


class Rx(object):
    def __init__(self):
        pass

    def connect_input(self, sender):
        pass

    def signal(self, sender, sig):
        global DONE
        #print(f"rx {sig} at {button_presses} {signals_ctr} {signals_processed}")
        if sig == LOW:
            DONE = True
            


class Empty(object):
    def __init__(self):
        pass

    def connect_input(self, sender):
        pass

    def signal(self, sender, sig):
        pass

mods = {}
lines = [x.strip() for x in open('cleaned_input','r')]
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
            if outmod == 'rx':
                mods[outmod] = Rx()
            else:
                mods[outmod] = Empty()
        mods[outmod].connect_input(mod)

import pickle
print(mods)
print(out_edges)

from collections import deque
import hashlib

signals_queue = deque()
signals_ctr = {LOW:0, HIGH:0}
signals_processed = 0
def process_signal(sender, signal, receiver, mods, out_edges, out_queue):
    global signals_processed
    signals_processed += 1
    res = mods[receiver].signal(sender, signal)
    if res is not None:
        #print("---", sender, signal, receiver, res)
        if receiver == 'rx':
            print("---", sender, signal, receiver, res)

        signals_ctr[res] += len(out_edges[receiver])
        for e in out_edges[receiver]:
            out_queue.append((receiver, res, e))


def bits_to_int(b):
    res = 0
    for bit in b:
        if bit:
            res = res * 2 + 1
    return res

for k,v in out_edges.items():
    for v2 in v:
        print(f"{k} -> {v2}")

BATCH_SIZE = 100
button_presses = 0
# &rg goes to rx
stateprint = ['qx','gz','hl','xt','ns','qf','sb','gj','tx','vz','xv']
while not DONE:
    #print(button_presses, bits_to_int(mods['rgans1'].state.values()), 
    #      bits_to_int(mods['rgans2'].state.values()), bits_to_int(mods['rgans3'].state.values()), bits_to_int(mods['rgans4'].state.values()))
    if button_presses % 10000 == 0:
        print(button_presses) 
    button_presses += 1
    signals_queue.append(("button", LOW, "broadcaster"))
    signals_ctr[LOW] += 1
    while len(signals_queue) > 0:
        batch_signals = deque()
        try:
            sender, signal, receiver = signals_queue.popleft()
        except IndexError:
            pass
        process_signal(sender, signal, receiver, mods, out_edges, signals_queue)

print(button_presses)
